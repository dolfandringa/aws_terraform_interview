variable "aws_region" {
  description = "The AWS region to install in"
  default     = "us-east-1"
  type        = string
}

variable "environment_long" {
  description = "The environment to install in"
  default     = "develop"
  type        = string
}

variable "environment_short" {
  description = "The environment to install in"
  type        = string
  default     = "dev"
}
