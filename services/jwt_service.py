from jwt import encode, decode
from dotenv import load_dotenv
import os

load_dotenv(".env")


def create_token(data: dict) -> str:
    return encode(
        payload=data,
        key=str(os.getenv("SECRET_KEY")),
        algorithm="HS256"
    )


def validate_token(token: str) -> dict:
    return decode(
        token,
        str(os.getenv("SECRET_KEY")),
        algorithms=["HS256"]
    )