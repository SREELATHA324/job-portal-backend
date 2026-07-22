from fastapi import APIRouter
from app.routers.user import users
from app.routers.job import jobs

router = APIRouter(
    prefix="/admin",
    tags=["Admin"]
)

@router.get("/dashboard")
def dashboard():
    return {
        "total_users": len(users),
        "total_managers": 0,
        "total_jobs": len(jobs),
        "applications": 0
    }

@router.get("/users")
def get_users():
    return {
        "users": users
    }

@router.get("/jobs")
def get_jobs():
    return {
        "jobs": jobs
    }

@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    return {
        "message": f"User {user_id} deleted successfully"
    }

@router.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    return {
        "message": f"Job {job_id} deleted successfully"
    }