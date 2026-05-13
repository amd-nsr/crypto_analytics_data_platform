resource "aws_iam_role" "glue_role" {
  name = "crypto-glue-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17",
    Statement = [{
      Effect = "Allow",
      Principal = { Service = "glue.amazonaws.com" },
      Action = "sts:AssumeRole"
    }]
  })
}


resource "aws_iam_policy" "glue_s3_policy" {
  name = "crypto-glue-s3-policy"

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Effect = "Allow",
        Action = ["s3:ListBucket"],
        Resource = "arn:aws:s3:::${var.bucket_name}"
      },
      {
        Effect = "Allow",
        Action = ["s3:GetObject","s3:PutObject"],
        Resource = "arn:aws:s3:::${var.bucket_name}/*"
      }
    ]
  })
}


resource "aws_iam_role_policy_attachment" "attach" {
  role       = aws_iam_role.glue_role.name
  policy_arn = aws_iam_policy.glue_s3_policy.arn
}
