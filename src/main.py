from fastapi import FastAPI
from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware
from api.routes.api import router as api_router
from core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, PROJECT_NAME, VERSION


def get_application() -> FastAPI:
    application = FastAPI(title=PROJECT_NAME, debug=DEBUG, version=VERSION)

    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=False,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()
