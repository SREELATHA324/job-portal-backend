from fastapi import APIRouter
from app.schemas.job import JobCreate
from app.routers.job import jobs

router = APIRouter(
    prefix="/manager",
    tags=["Manager"]
)


from pydantic import BaseModel
from typing import Optional

class CompanySchema(BaseModel):
    name: str
    website: Optional[str] = ""
    description: Optional[str] = ""

current_company = {
    "name": "Shnoor Technologies",
    "website": "https://shnoor.com",
    "description": "Leading software solutions and IT technology company."
}


@router.get("/company")
def get_company():
    return {
        "company": current_company
    }


@router.post("/company")
def register_company(company: CompanySchema):
    global current_company
    current_company = {
        "name": company.name,
        "website": company.website or "",
        "description": company.description or ""
    }
    return {
        "message": "Company Registered Successfully",
        "company": current_company
    }


@router.post("/jobs")
def create_job(job: JobCreate):
    jobs.append(job)
    return {
        "message": "Job Posted Successfully",
        "job": job
    }


@router.get("/applicants")
def view_applicants():
    return {
        "applicants": [
            {
                "name": "Sreelatha",
                "email": "sree@gmail.com",
                "ats_score": 85,
                "status": "Accepted"
            }
        ]
    }


@router.put("/jobs/{job_id}")
def edit_job(job_id: int):
    return {
        "message": f"Job {job_id} Updated Successfully"
    }


@router.delete("/jobs/{job_id}")
def delete_job(job_id: int):
    return {
        "message": f"Job {job_id} Deleted Successfully"
    }


@router.put("/applicants/{candidate_id}/shortlist")
def shortlist_candidate(candidate_id: int):
    return {
        "message": f"Candidate {candidate_id} Shortlisted Successfully"
    }


@router.put("/applicants/{candidate_id}/reject")
def reject_candidate(candidate_id: int):
    return {
        "message": f"Candidate {candidate_id} Rejected Successfully"
    }