resource "aws_cloudwatch_log_group" "glue_logs" {
  name = "/aws/glue/crypto-etl"
}

resource "aws_cloudwatch_metric_alarm" "glue_failures" {
  alarm_name = "glue-failure"

  namespace   = "AWS/Glue"
  metric_name = "glue.driver.aggregate.numFailedTasks"

  statistic = "Sum"
  period    = 300
  threshold = 1

  comparison_operator = "GreaterThanOrEqualToThreshold"
  evaluation_periods  = 1
}
