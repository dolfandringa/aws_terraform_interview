from typing import Any

from authorizer_lambda.cognito_adapter import fetch_owner_from_cognito
from authorizer_lambda.config import Settings, config
from authorizer_lambda.models import (
    AuthorizationResponse,
    OwnerResponse,
    TokenAuthorizationRequest,
    OwnerRequest,
    PolicyDocument,
    PolicyStatement,
    StatementEffect,
)
import jwt


def get_owner_uuid(cognito_id: str, settings: Settings) -> str:
    """Retrieve the owner_uuid from the lambda based on the cognito id and return it."""
    request = OwnerRequest(cognito_id=cognito_id)
    cognito_object = fetch_owner_from_cognito(cognito_id)
    # get this from the lambda
    # response: OwnerResponse = ...
    return cognito_object.owner_uuid


def verify_dev_token(jwt_token: str) -> str:
    decoded_token = jwt.decode(jwt_token, config.dev_jwt_secret, algorithms=["HS256"])

    if decoded_token.get("owner_uuid"):
        return decoded_token["owner_uuid"]
    else:
        raise Exception("Invalid dev token")


def verify_cognito_token(jwt_token: str) -> str:
    decoded_token = jwt.decode(jwt_token, config.public_rsa_key, algorithms=["RS256"])
    owner_uuid = get_owner_uuid(decoded_token.get("sub"), config)

    return owner_uuid


def authorize_request(owner_uuid: str) -> AuthorizationResponse:
    resource = f"arn:aws:execute-api:us-east-1:349228585176:aovoxtdoh3/backend_api_gw_stage_dev/ANY/api/{owner_uuid}/*"

    return AuthorizationResponse(
        principalId=owner_uuid,
        policyDocument=PolicyDocument(
            Version="2012-10-17",
            Statement=[
                PolicyStatement(
                    Action="execute-api:Invoke",
                    Effect=StatementEffect.ALLOW,
                    Resource=resource,
                )
            ],
        ),
        context={},
    )


def handler(event, context) -> dict[str, Any]:
    """
    Handle the incoming authorization requests, verify the token and return the
    policy for API Gateway
    """

    authorization_request: TokenAuthorizationRequest = (
        TokenAuthorizationRequest.parse_obj(event)
    )
    parsed_token = jwt.decode(
        authorization_request.authorizationToken, options={"verify_signature": False}
    )

    is_cognito_token = parsed_token.get("sub")

    if is_cognito_token:
        decoded_token = verify_cognito_token(authorization_request.authorizationToken)
    else:
        decoded_token = verify_dev_token(authorization_request.authorizationToken)

    return authorize_request(decoded_token).dict()
