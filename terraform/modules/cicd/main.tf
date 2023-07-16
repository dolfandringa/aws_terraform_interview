resource "aws_s3_bucket" "deployment" {
  bucket = "${var.lambda_deployment_bucket_base_name}-${var.environment}"
  tags   = var.module_tags
}
