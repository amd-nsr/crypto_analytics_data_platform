resource "aws_redshiftserverless_namespace" "crypto" {
  namespace_name = "crypto"
  db_name        = var.redshift_db
}

resource "aws_redshiftserverless_workgroup" "crypto" {
  workgroup_name = "crypto-wg"
  namespace_name  = aws_redshiftserverless_namespace.crypto.namespace_name
}
