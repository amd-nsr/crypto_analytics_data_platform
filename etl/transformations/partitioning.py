from pyspark.sql.functions import (
    year,
    month,
    dayofmonth,
    col
)

def add_partitions(df):

    return (
        df
        .withColumn(
            "year",
            year(col("timestamp"))
        )
        .withColumn(
            "month",
            month(col("timestamp"))
        )
        .withColumn(
            "day",
            dayofmonth(col("timestamp"))
        )
    )
