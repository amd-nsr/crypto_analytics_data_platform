import boto3

from warehouse.config.settings import (
    S3_BUCKET
)

s3_client = boto3.client("s3")


def get_latest_partition():

    response = (
        s3_client.list_objects_v2(
            Bucket=S3_BUCKET,
            Prefix="curated/crypto_prices/",
            Delimiter="/"
        )
    )

    prefixes = []

    for obj in response.get(
        "CommonPrefixes",
        []
    ):
        prefixes.append(
            obj["Prefix"]
        )

    if not prefixes:
        raise Exception(
            "No partitions found"
        )

    return sorted(prefixes)[-1]
