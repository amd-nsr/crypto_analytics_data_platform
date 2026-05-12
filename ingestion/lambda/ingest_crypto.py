from ingestion.clients.crypto_api_client import (
    fetch_crypto_prices
)

from ingestion.validators.payload_validator import (
    validate_payload
)

from ingestion.services.partitioning import (
    build_raw_partition
)

from ingestion.services.s3_writer import (
    write_json_to_s3
)

from ingestion.shared.logger import get_logger

logger = get_logger(__name__)


def lambda_handler(event, context):

    logger.info("Starting crypto ingestion")

    # ==========================================
    # 1. FETCH DATA
    # ==========================================

    records = fetch_crypto_prices()

    logger.info(f"Fetched {len(records)} records")

    # ==========================================
    # 2. VALIDATE
    # ==========================================

    validate_payload(records)

    logger.info("Payload validation successful")

    # ==========================================
    # 3. BUILD PARTITION
    # ==========================================

    partition = build_raw_partition()

    logger.info(f"Partition: {partition}")

    # ==========================================
    # 4. WRITE TO S3
    # ==========================================

    s3_key = write_json_to_s3(
        data=records,
        partition=partition
    )

    logger.info(f"Data written to S3: {s3_key}")

    # ==========================================
    # DONE
    # ==========================================

    logger.info("Ingestion completed successfully")

    return {
        "statusCode": 200,
        "body": {
            "records": len(records),
            "s3_key": s3_key
        }
    }