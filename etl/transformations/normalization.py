from pyspark.sql.functions import (
    col,
    to_timestamp
)

def normalize_columns(df):

    return (
        df
        .withColumn(
            "price",
            col("price").cast("double")
        )
        .withColumn(
            "timestamp",
            to_timestamp(col("timestamp"))
        )
        .select(
            "symbol",
            "price",
            "timestamp"
        )
    )
