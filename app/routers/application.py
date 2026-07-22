from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime

router = APIRouter(
    prefix="/applications",
    tags=["Applications"]
)

applications = []


class ApplicationCreate(BaseModel):
    job_id: int
    resume_url: str
    cover_letter: str


@router.post("/")
def apply_job(application: ApplicationCreate):
    new_application = {
        "id": len(applications) + 1,
        "job_id": application.job_id,
        "resume_url": application.resume_url,
        "cover_letter": application.cover_letter,
        "job_title": f"Job {application.job_id}",
        "company_name": "Demo Company",
        "applied_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "status": "Pending"
    }

    applications.append(new_application)

    return {
        "message": "Application submitted successfully",
        "application": new_application
    }


@router.get("/my")
def get_my_applications():
    return {
        "applications": applications
    }