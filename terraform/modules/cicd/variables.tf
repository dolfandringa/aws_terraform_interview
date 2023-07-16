variable "module_tags" {
  default = {
    Application = "cicd"
  }
  description = "Tags for this module"
  type        = map(string)
}

variable "environment" {
  description = "Environment where the module is deployed"
  type        = string
  nullable    = false
}

variable "lambda_deployment_bucket_base_name" {
  description = "Name of the bucket to store the built lambdas in"
  type        = string
  nullable    = false
  default     = "dolfs-deployment-lambdas"
}
