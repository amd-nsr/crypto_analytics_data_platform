from pyspark.sql import SparkSession

def read_raw_json(
    spark: SparkSession,
    path: str,
    schema
):

    return (
        spark.read
        .schema(schema)
        .json(path)
    )
