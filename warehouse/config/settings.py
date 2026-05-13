import os
from dotenv import load_dotenv

load_dotenv()

S3_BUCKET = os.getenv("S3_BUCKET")

REDSHIFT_DATABASE = os.getenv("REDSHIFT_DATABASE")
REDSHIFT_WORKGROUP = os.getenv("REDSHIFT_WORKGROUP")
REDSHIFT_SECRET_ARN = os.getenv("REDSHIFT_SECRET_ARN")
REDSHIFT_COPY_ROLE = os.getenv("REDSHIFT_COPY_ROLE")
