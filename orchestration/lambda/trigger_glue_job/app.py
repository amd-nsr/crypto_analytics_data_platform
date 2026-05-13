import os
import boto3

glue_client = boto3.client("glue")

GLUE_JOB_NAME = os.environ[
    "GLUE_JOB_NAME"
]


def lambda_handler(event, context):

    response = glue_client.start_job_run(
        JobName=GLUE_JOB_NAME
    )

    return {
        "job_run_id": response["JobRunId"]
    }
