import json
import boto3
from datetime import datetime, timezone

from ingestion.config.settings import S3_BUCKET

s3_client = boto3.client("s3")

def write_json_to_s3(data, partition):

    timestamp = datetime.now(timezone.utc).isoformat()

    key = (
        f"raw/{partition}"
        f"data_{timestamp}.json"
    )

    s3_client.put_object(
        Bucket=S3_BUCKET,
        Key=key,
        Body=json.dumps(data),
        ContentType="application/json"
    )

    return key
