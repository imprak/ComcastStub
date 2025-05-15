from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi import Depends, HTTPException, status


security = HTTPBasic()


class Security:
    def __call__(self, credentials: HTTPBasicCredentials = Depends(security)):
        if (
            not credentials.username
            or not credentials.password
            or credentials.username != "admin"
        ):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail={
                    "type": "basic auth",
                    "status": "403",
                    "title": "AUTHORIZATION ERROR",
                    "detail": "Incorrect username or password",
                },
            )

        return credentials.username
