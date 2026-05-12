
def validate_dataframe(df):

    if df.count() == 0:
        raise Exception(
            "DataFrame is empty"
        )
