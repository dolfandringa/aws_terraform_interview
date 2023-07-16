<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.4.6 |
| <a name="requirement_archive"></a> [archive](#requirement\_archive) | ~> 2.2.0 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 4.64.0 |
| <a name="requirement_random"></a> [random](#requirement\_random) | ~> 3.1.0 |

## Providers

No providers.

## Modules

| Name | Source | Version |
|------|--------|---------|
| <a name="module_cicd"></a> [cicd](#module\_cicd) | ../../modules/cicd | n/a |

## Resources

No resources.

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_aws_region"></a> [aws\_region](#input\_aws\_region) | The AWS region to install in | `string` | `"us-east-1"` | no |
| <a name="input_environment_long"></a> [environment\_long](#input\_environment\_long) | The environment to install in | `string` | `"develop"` | no |
| <a name="input_environment_short"></a> [environment\_short](#input\_environment\_short) | The environment to install in | `string` | `"dev"` | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->