import json
from pathlib import Path

import jwt
import pytest

from authorizer_lambda.config import config
from authorizer_lambda.main import verify_dev_token


def test_return_owner_uuid_dev(mocker):
    mock_jwt_decode = mocker.patch.object(jwt, "decode")
    mock_jwt_decode.return_value = {"owner_uuid": "a-b-c-d"}
    request = Path(__file__).parent / Path("data/authorization_request.json")
    request = json.load(request.open("rt"))
    token = request["authorizationToken"]

    response = verify_dev_token(token)

    expected = "a-b-c-d"

    assert response == expected
    mock_jwt_decode.assert_called_once_with(token, config.dev_jwt_secret, algorithms=["HS256"])


def test_raise_exception_when_no_owner_uuid_dev(mocker):
    mock_jwt_decode = mocker.patch.object(jwt, "decode")
    mock_jwt_decode.return_value = {}
    request = Path(__file__).parent / Path("data/authorization_request.json")
    request = json.load(request.open("rt"))
    token = request["authorizationToken"]

    with pytest.raises(Exception) as e:
        verify_dev_token(token)

    assert str(e.value) == "Invalid dev token"
