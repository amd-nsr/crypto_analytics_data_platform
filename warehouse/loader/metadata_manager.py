from warehouse.services.redshift_client import (
    execute_sql,
    wait_for_query,
    redshift_client
)


def partition_already_loaded(
    partition_path
):

    sql = f"""
    SELECT COUNT(*)
    FROM crypto.etl_metadata
    WHERE partition_path = '{partition_path}'
    ;
    """

    statement_id = execute_sql(sql)

    wait_for_query(statement_id)

    result = (
        redshift_client.get_statement_result(
            Id=statement_id
        )
    )

    count = int(
        result["Records"][0][0]["longValue"]
    )

    return count > 0


def record_partition_load(
    partition_path
):

    sql = f"""
    INSERT INTO crypto.etl_metadata (
        partition_path
    )
    VALUES (
        '{partition_path}'
    );
    """

    statement_id = execute_sql(sql)

    wait_for_query(statement_id)

