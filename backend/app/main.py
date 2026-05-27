from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import experience
from app.core.config import settings


app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="API backend pour la plateforme WebAR par QR code.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.frontend_origin],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(experience.router, prefix=settings.api_prefix, tags=["Experiences"])


@app.get("/")
def health_check():
    return {
        "status": "ok",
        "message": "Backend WebAR operationnel",
    }
