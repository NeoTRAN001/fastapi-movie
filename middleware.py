from fastapi.security import HTTPBearer
from fastapi import Request, HTTPException, status

import services.jwt_service


class JWTBearer(HTTPBearer):

    async def __call__(self, req: Request):
        auth = await super().__call__(req)
        token_validate = services.jwt_service.validate_token(auth.credentials)

        if not token_validate:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Invalid credentials")