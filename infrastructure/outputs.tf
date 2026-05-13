output "s3_bucket" {
  value = aws_s3_bucket.data_lake.bucket
}

output "glue_job" {
  value = aws_glue_job.crypto_etl.name
}
