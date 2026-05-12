from datetime import datetime, timezone

def build_raw_partition():

    now = datetime.now(timezone.utc)

    return (
        f"year={now.year}/"
        f"month={now.month}/"
        f"day={now.day}/"
    )
