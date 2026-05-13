from warehouse.config.settings import (
    S3_BUCKET,
    REDSHIFT_COPY_ROLE
)

from warehouse.services.s3_discovery import (
    get_latest_partition
)

from warehouse.services.redshift_client import (
    execute_sql,
    wait_for_query
)

from warehouse.loader.metadata_manager import (
    partition_already_loaded,
    record_partition_load
)

from warehouse.shared.logger import get_logger

logger = get_logger(__name__)


def run_incremental_load():

    logger.info(
        "Starting warehouse load"
    )

    # ==========================================
    # 1. FIND LATEST PARTITION
    # ==========================================

    latest_partition = (
        get_latest_partition()
    )

    logger.info(
        f"Latest partition: {latest_partition}"
    )

    s3_path = (
        f"s3://{S3_BUCKET}/"
        f"{latest_partition}"
    )

    # ==========================================
    # 2. CHECK METADATA
    # ==========================================

    already_loaded = (
        partition_already_loaded(
            latest_partition
        )
    )

    if already_loaded:

        logger.info(
            "Partition already loaded"
        )

        return

    # ==========================================
    # 3. COPY INTO STAGING
    # ==========================================

    copy_sql = f"""
    COPY crypto.stg_crypto_prices
    FROM '{s3_path}'
    IAM_ROLE '{REDSHIFT_COPY_ROLE}'
    FORMAT AS PARQUET;
    """

    logger.info(
        "Running COPY"
    )

    statement_id = execute_sql(
        copy_sql
    )

    wait_for_query(statement_id)

    # ==========================================
    # 4. MERGE INTO FACT
    # ==========================================

    # merge_sql = """
    # MERGE INTO crypto.fact_crypto_prices target
    # USING crypto.stg_crypto_prices source

    # ON target.symbol = source.symbol
    # AND target.timestamp = source.timestamp

    # WHEN NOT MATCHED THEN

    # INSERT (
    #     symbol,
    #     price,
    #     timestamp,
    #     year,
    #     month,
    #     day
    # )

    # VALUES (
    #     source.symbol,
    #     source.price,
    #     source.timestamp,
    #     source.year,
    #     source.month,
    #     source.day
    # );
    # """

    merge_sql = """
        DELETE FROM crypto.fact_crypto_prices AS f
        USING crypto.stg_crypto_prices AS s
        WHERE f.symbol = s.symbol
        AND f."timestamp" = s."timestamp";

        -- Step 2: insert fresh data
        INSERT INTO crypto.fact_crypto_prices (
            symbol,
            price,
            "timestamp"
        )
        SELECT
            symbol,
            price,
            "timestamp"
        FROM crypto.stg_crypto_prices;
        """

    logger.info(
        "Running MERGE"
    )

    statement_id = execute_sql(
        merge_sql
    )

    wait_for_query(statement_id)

    # ==========================================
    # 5. RECORD METADATA
    # ==========================================

    logger.info(
        "Recording metadata"
    )

    record_partition_load(
        latest_partition
    )

    # ==========================================
    # 6. CLEAN STAGING
    # ==========================================

    truncate_sql = """
    TRUNCATE TABLE
    crypto.stg_crypto_prices;
    """

    statement_id = execute_sql(
        truncate_sql
    )

    wait_for_query(statement_id)

    logger.info(
        "Warehouse load completed"
    )


if __name__ == "__main__":

    run_incremental_load()
