resource "aws_sfn_state_machine" "pipeline" {
  name     = "crypto-pipeline"
  role_arn = var.stepfn_role_arn

  definition = jsonencode({
    StartAt = "GlueETL",

    States = {
      GlueETL = {
        Type     = "Task",
        Resource = "arn:aws:states:::glue:startJobRun.sync",
        Parameters = {
          JobName = var.glue_job_name
        },
        Next = "RedshiftLoad"
      },

      RedshiftLoad = {
        Type = "Task",
        Resource = "arn:aws:states:::lambda:invoke",
        Parameters = {
          FunctionName = var.lambda_name
        },
        End = true
      }
    }
  })
}
