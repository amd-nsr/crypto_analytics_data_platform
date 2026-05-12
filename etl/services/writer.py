
def write_curated_parquet(
    df,
    output_path
):

    (
        df.write
        .mode("append")
        .partitionBy(
            "year",
            "month",
            "day"
        )
        .parquet(output_path)
    )
