## Authorization Lambda

This lambda handles AWS API-gateway authorization requests and returns a policy based on a JWT token.

It should:
* handle dev JWT tokens with a symmetric JWT secret
* validate 2 different JWT tokens from different sources:
  * A dev token manually created by us, with a symmetric `HS256` secret
  * A [JWT token from AWS cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html) with a `sub` attribute (==cognito user id). Assume the cognito token is also signed by a (different) HS256 symmetric secret
* Get the owner_uuid for the user:
  * For the dev token, retrieve the owner_uuid from the JWT token payload
  * For cognito, retrieve the owner_uuid by calling the backend lambda using the cognito `sub` property form the payload as `cognito_id`
* Create a policy on the methodArn, allowing `arn:aws:execute-api:us-east-1:349228585176:aovoxtdoh3/sunrise_backend_api_gw_stage_dev/ANY/api/{owner_uuid}/*`
Make sure to also include tests.

For API Gateway authorizer lambdas, this is the expected input and output:
* https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-input.html
* https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-lambda-authorizer-output.html
* https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-use-lambda-authorizer.html

JWT:
* https://jwt.io/
* https://pyjwt.readthedocs.io/en/latest/usage.html

Boto3:
* https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/lambda/client/invoke.html

## Bonus
* How do you actually verify Cognito JWT tokens?
