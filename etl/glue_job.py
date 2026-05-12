from pyspark.sql import SparkSession

# from etl.config.settings import (
#     S3_BUCKET
# )

from etl.schema.crypto_schema import (
    CRYPTO_SCHEMA
)

from etl.services.reader import (
    read_raw_json
)

from etl.transformations.cleaning import (
    remove_null_prices
)

from etl.transformations.normalization import (
    normalize_columns
)

from etl.transformations.partitioning import (
    add_partitions
)

from etl.services.validators import (
    validate_dataframe
)

from etl.services.writer import (
    write_curated_parquet
)

from etl.shared.logger import get_logger

logger = get_logger(__name__)


S3_BUCKET="nsr-crypto-prices-data"

RAW_PATH = (
    f"s3://{S3_BUCKET}/raw/"
)

CURATED_PATH = (
    f"s3://{S3_BUCKET}/curated/crypto_prices/"
)


def run_etl():

    logger.info(
        "Starting ETL job"
    )

    spark = (
        SparkSession.builder
        .appName("CryptoETL")
        .getOrCreate()
    )

    # ==========================================
    # 1. READ RAW DATA
    # ==========================================

    df = read_raw_json(
        spark=spark,
        path=RAW_PATH,
        schema=CRYPTO_SCHEMA
    )

    logger.info(
        f"Raw records: {df.count()}"
    )

    # ==========================================
    # 2. CLEANING
    # ==========================================

    df = remove_null_prices(df)

    # ==========================================
    # 3. NORMALIZATION
    # ==========================================

    df = normalize_columns(df)

    # ==========================================
    # 4. PARTITIONING
    # ==========================================

    df = add_partitions(df)

    # ==========================================
    # 5. VALIDATION
    # ==========================================

    validate_dataframe(df)

    # ==========================================
    # 6. WRITE CURATED DATA
    # ==========================================

    write_curated_parquet(
        df=df,
        output_path=CURATED_PATH
    )

    logger.info(
        "ETL completed successfully"
    )


if __name__ == "__main__":
    run_etl()
