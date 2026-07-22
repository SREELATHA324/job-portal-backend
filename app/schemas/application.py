from pydantic import BaseModel

class JobApplication(BaseModel):
    job_id: int
    applicant_name: str
    email: str
    resume: str
    ats_score: int