resource "aws_lambda_function" "redshift_loader" {
  function_name = "crypto-redshift-loader"
  role          = var.lambda_role_arn
  runtime       = "python3.11"
  handler       = "lambda_function.lambda_handler"

  filename = "lambda.zip"

  environment {
    variables = {
      REDSHIFT_WORKGROUP = var.redshift_workgroup
      REDSHIFT_DATABASE   = var.redshift_db
      REDSHIFT_SECRET_ARN = var.redshift_secret
      S3_BUCKET           = var.bucket_name
    }
  }
}
