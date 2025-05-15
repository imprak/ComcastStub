from fastapi import FastAPI, status
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware

from app.endpoints import (
    isp_endpoints,
    scn_profile_endpoints,
    osp_config_endpoints,
    osp_activation_endpoints,
)

app = FastAPI(title="Comcast-Stub")

app.include_router(isp_endpoints.router)
app.include_router(scn_profile_endpoints.router)
app.include_router(osp_config_endpoints.router)
app.include_router(osp_activation_endpoints.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(RequestValidationError)
async def convert_422_into_400(request, exc: RequestValidationError):
    raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST,
        detail={
            "type": "validation error",
            "status": "400",
            "title": "VALIDATION ERROR",
            "detail": str(exc),
        },
    )


@app.get("/", include_in_schema=False)
def redirect():
    return RedirectResponse(url="/docs")


# For local test
import uvicorn

uvicorn.run(app)
