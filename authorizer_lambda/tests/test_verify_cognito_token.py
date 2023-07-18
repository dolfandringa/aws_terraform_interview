import json
from datetime import datetime
from pathlib import Path

import jwt

from authorizer_lambda import cognito_adapter
from authorizer_lambda.config import config
from authorizer_lambda.main import verify_cognito_token, get_owner_uuid
from authorizer_lambda.models import CognitoResponse


def test_return_owner_uuid_cognito(mocker):
    mock_jwt_decode = mocker.patch.object(jwt, "decode")
    mock_jwt_decode.return_value = {"sub": "a-b-c-d"}

    request = Path(__file__).parent / Path("data/authorization_request.json")
    request = json.load(request.open("rt"))
    token = request["authorizationToken"]

    response = verify_cognito_token(token)

    expected = "ce4291d7-2604-41bb-ae61-c9cee3d38402"

    assert response == expected
    mock_jwt_decode.assert_called_once_with(token, config.public_rsa_key, algorithms=["RS256"])


def test_fetch_owner_from_cognito(mocker):
    mock_generate_cognito_response = mocker.patch.object(cognito_adapter, "fetch_owner_from_cognito")
    mock_generate_cognito_response.return_value = CognitoResponse(
        sub="a-b-c-d",
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
        owner_uuid="a-b-c-d"
    )

    response = get_owner_uuid("a-b-c-d", config)

    expected = "a-b-c-d"

    assert response == expected
    mock_generate_cognito_response.assert_called_once_with("a-b-c-d")
