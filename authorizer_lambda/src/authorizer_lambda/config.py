import os
from pathlib import Path

from pydantic import BaseSettings


root_dir = Path(__file__).parent.parent.parent


class Settings(BaseSettings):
    """Configuration"""

    class Config:
        env_file = ".env"

    cognito_user_pool_id: str = "some_user_pool_id"
    dev_jwt_secret: str = "some_secret"
    backend_lambda_arn = (
        "arn:aws:lambda:us-east-1:11111111111:function:some-backend-lambda-dev"
    )
    public_rsa_key = open(
        os.path.join(root_dir, "id_rsa.pub"), "r"
    ).read()  # assuming this will come from the KMS


config = Settings()
