import jwt.exceptions
from jwt import encode, decode
from dotenv import load_dotenv
import os


class JWTService:

    def __init__(self) -> None:
        load_dotenv(".env")

    def create_token(self, data: dict) -> str:
        return encode(
            payload=data,
            key=str(os.getenv("SECRET_KEY")),
            algorithm="HS256"
        )

    def decode_token(self, token: str) -> dict:
        return decode(
            token,
            str(os.getenv("SECRET_KEY")),
            algorithms=["HS256"]
        )

    def validate_token(self, token: str) -> bool:
        try:
            decode(token, str(os.getenv("SECRET_KEY")), algorithms=["HS256"])
            return True
        except jwt.exceptions.DecodeError:
            return False
