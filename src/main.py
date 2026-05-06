import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from fastapi.middleware.cors import CORSMiddleware
from src.core.database import Base, engine
from src.modules.frete.router import router as frete_router
from src.modules.auth.router import router as auth_router

# Ensure static directory exists
os.makedirs("static", exist_ok=True)

# Database table creation
Base.metadata.create_all(bind=engine)

app = FastAPI(title="TransCarga API")

# Add CORS middleware — must be added before any routes/mounts
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_origin_regex=r"^https?://(localhost|127\.0\.0\.1)(:\d+)?$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# Include domain routers BEFORE static mount
app.include_router(frete_router)
app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "TransCarga API is Running", "version": "1.0.0"}

# Static files mount AFTER routers (mounts can intercept middleware)
app.mount("/static", StaticFiles(directory="static"), name="static")

