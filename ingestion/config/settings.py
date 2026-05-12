import os
from dotenv import load_dotenv

load_dotenv()

AWS_REGION = os.getenv("AWS_REGION")

S3_BUCKET = os.getenv("S3_BUCKET")

API_URL = os.getenv("API_URL")
