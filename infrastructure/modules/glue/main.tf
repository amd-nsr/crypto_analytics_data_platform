resource "aws_glue_job" "crypto_etl" {
  name     = "crypto-etl-job"
  role_arn = var.glue_role_arn

  command {
    script_location = "s3://${var.bucket_name}/scripts/glue_etl.py"
    python_version  = "3"
  }

  glue_version = "4.0"
  max_retries  = 1

  default_arguments = {
    "--enable-metrics" = "true"
    "--job-bookmark-option" = "job-bookmark-enable"
  }
}
