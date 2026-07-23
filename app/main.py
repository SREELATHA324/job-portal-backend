import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.auth import router as auth_router
from app.routers.job import router as job_router
from app.routers.manager import router as manager_router
from app.routers.user import router as user_router
from app.routers.admin import router as admin_router
from app.routers.application import router as application_router

app = FastAPI(title="Job Portal Backend")

origins = [

    "https://job-portal-frontend-rys7.onrender.com",

    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:5174",
    "http://localhost:5175",
    "http://localhost:5176",
    "http://localhost:5177",
    "http://localhost:5178",
    "http://localhost:5179",
    "http://localhost:5187"

    "http://127.0.0.1:3000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:5175",
    "http://127.0.0.1:5176",
    "http://127.0.0.1:5177",
    "http://127.0.0.1:5178",
    "http://127.0.0.1:5179",
    "http://127.0.0.1:5186",
    "http://127.0.0.1:5187",
]

env_origins = os.getenv("ALLOWED_ORIGINS")
if env_origins:
    for item in env_origins.split(","):
        item = item.strip()
        if item and item not in origins:
            origins.append(item)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5174", "http://127.0.0.1:5174"],
    allow_origin_regex=r"http://127.0.0.1:5174",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(job_router)
app.include_router(manager_router)
app.include_router(user_router)
app.include_router(admin_router)
app.include_router(application_router)


@app.get("/")
def home():
    return {
        "message": "Job Portal Backend Running"
    }