import boto3

from warehouse.config.settings import (
    REDSHIFT_WORKGROUP,
    REDSHIFT_DATABASE,
    REDSHIFT_SECRET_ARN
)

redshift_client = boto3.client(
    "redshift-data"
)


def execute_sql(sql):

    response = (
        redshift_client.execute_statement(
            WorkgroupName=REDSHIFT_WORKGROUP,
            Database=REDSHIFT_DATABASE,
            SecretArn=REDSHIFT_SECRET_ARN,
            Sql=sql
        )
    )

    return response["Id"]



def wait_for_query(statement_id):

    while True:

        response = (
            redshift_client.describe_statement(
                Id=statement_id
            )
        )

        status = response["Status"]

        if status in [
            "FINISHED",
            "FAILED",
            "ABORTED"
        ]:

            if status != "FINISHED":
                raise Exception(response)

            return response
