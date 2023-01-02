from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from schemas.user_schema import UserAccount
from services.jwt_service import JWTService

router = APIRouter()


@router.post('/login', tags=['auth'])
def login(user: UserAccount):

    if user.email == "admin@gmail.com" and user.password == "admin":
        return JSONResponse(
            content={"token": JWTService().create_token(user.dict())},
            status_code=status.HTTP_202_ACCEPTED
        )

    return JSONResponse(content={"message": "Email o contraseña no valido"}, status_code=status.HTTP_400_BAD_REQUEST)
