terraform {

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.64.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1.0"
    }
    archive = {
      source  = "hashicorp/archive"
      version = "~> 2.2.0"
    }
  }

  required_version = "~> 1.4.6"
}


provider "aws" {
  region = var.aws_region

  default_tags {
    tags = {
      Environment = var.environment_long
    }
  }
}
