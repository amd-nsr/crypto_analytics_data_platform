from warehouse.loader.incremental_loader import (
    run_incremental_load
)


def lambda_handler(event, context):

    run_incremental_load()

    return {
        "status": "success"
    }
