from pyspark.sql.functions import col

def remove_null_prices(df):

    return df.filter(
        col("price").isNotNull()
    )
