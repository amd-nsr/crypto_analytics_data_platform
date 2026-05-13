resource "aws_glue_catalog_database" "crypto" {
  name = "crypto"
}

resource "aws_glue_catalog_table" "crypto_prices" {
  name          = "crypto_prices"
  database_name = aws_glue_catalog_database.crypto.name

  table_type = "EXTERNAL_TABLE"

  storage_descriptor {
    location = "s3://${var.bucket_name}/curated/crypto_prices/"

    input_format  = "org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat"
    output_format = "org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat"

    serde_info {
      serialization_library = "org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe"
    }

    columns { name = "symbol" type = "string" }
    columns { name = "price" type = "double" }
    columns { name = "timestamp" type = "timestamp" }
    columns { name = "year" type = "int" }
    columns { name = "month" type = "int" }
    columns { name = "day" type = "int" }
  }
}
