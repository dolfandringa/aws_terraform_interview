<!-- BEGIN_TF_DOCS -->
## Requirements

| Name | Version |
|------|---------|
| <a name="requirement_terraform"></a> [terraform](#requirement\_terraform) | ~> 1.4.6 |
| <a name="requirement_aws"></a> [aws](#requirement\_aws) | ~> 4.64.0 |

## Providers

| Name | Version |
|------|---------|
| <a name="provider_aws"></a> [aws](#provider\_aws) | ~> 4.64.0 |

## Modules

No modules.

## Resources

| Name | Type |
|------|------|
| [aws_s3_bucket.deployment](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket) | resource |

## Inputs

| Name | Description | Type | Default | Required |
|------|-------------|------|---------|:--------:|
| <a name="input_environment"></a> [environment](#input\_environment) | Environment where the module is deployed | `string` | n/a | yes |
| <a name="input_lambda_deployment_bucket_base_name"></a> [lambda\_deployment\_bucket\_base\_name](#input\_lambda\_deployment\_bucket\_base\_name) | Name of the bucket to store the built lambdas in | `string` | `"dolfs-deployment-lambdas"` | no |
| <a name="input_module_tags"></a> [module\_tags](#input\_module\_tags) | Tags for this module | `map(string)` | <pre>{<br>  "Application": "cicd"<br>}</pre> | no |

## Outputs

No outputs.
<!-- END_TF_DOCS -->