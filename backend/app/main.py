import logging

from fastapi import FastAPI

from starlette.middleware.cors import CORSMiddleware

from app.features.login import login_router
from app.features.device import device_router

# Top Level Configurations
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Fast API Configuratinos
app = FastAPI(
    title="backend",
    openapi_url="/v1/openapi.json",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(login_router, prefix="/api/v1")
app.include_router(device_router, prefix="/api/v1")
