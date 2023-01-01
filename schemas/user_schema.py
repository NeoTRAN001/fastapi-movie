from pydantic import BaseModel


class UserAccount(BaseModel):
    email: str
    password: str
