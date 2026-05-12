from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    DoubleType
)

CRYPTO_SCHEMA = StructType([

    StructField(
        "symbol",
        StringType(),
        True
    ),

    StructField(
        "price",
        DoubleType(),
        True
    ),

    StructField(
        "timestamp",
        StringType(),
        True
    )
])
