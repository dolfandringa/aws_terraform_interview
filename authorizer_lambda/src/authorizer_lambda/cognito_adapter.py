from datetime import datetime

from authorizer_lambda.models import CognitoResponse


def fetch_owner_from_cognito(cognito_id: str) -> CognitoResponse:
    return CognitoResponse(
        sub=cognito_id,
        device_key="d5a5744b-5090-4207-b0c9-ec711d23916e",
        iss="https://cognito-idp.us-east-1.amazonaws.com/authorizer_lambda",
        version=2,
        client_id="xxxxxxxxxxxxexample",
        origin_jti="0d061e49-5d8e-4d73-a648-61dcb1436a14",
        event_id="9428e451-b170-40d9-82b6-7c91091e9319",
        token_use="access",
        scope="phone openid profile resourceserver.1/appclient2 email",
        auth_time=datetime.now().timestamp(),
        exp=datetime.now().timestamp() + 3600,
        iat=datetime.now().timestamp(),
        jti="49706b7e-fb12-4e2d-9eff-6bbf3c7739cb",
        owner_uuid="ce4291d7-2604-41bb-ae61-c9cee3d38402",
    )
