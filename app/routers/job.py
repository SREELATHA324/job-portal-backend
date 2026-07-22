from fastapi import APIRouter, HTTPException
from app.schemas.job import JobCreate

router = APIRouter(prefix="/jobs", tags=["Jobs"])

jobs = [
    JobCreate(
        title="Frontend Developer",
        description="We are looking for a skilled React.js frontend developer to build responsive user interfaces.",
        location="Bengaluru, KA",
        salary=900000,
        job_type="Full Time",
        skills="React, JavaScript, TailwindCSS, HTML/CSS"
    ),
    JobCreate(
        title="Full Stack Python Developer",
        description="Join our engineering team to build scalable FastAPI web APIs and modern web applications.",
        location="Mumbai, MH",
        salary=1150000,
        job_type="Full Time",
        skills="Python, FastAPI, React, PostgreSQL"
    ),
    JobCreate(
        title="UI/UX Designer",
        description="Design intuitive user journeys, wireframes, and high-fidelity mockups for our web platform.",
        location="Hyderabad, TS",
        salary=850000,
        job_type="Contract",
        skills="Figma, UI Design, Prototyping"
    ),
    JobCreate(
        title="Data Analyst",
        description="Analyze key product metrics, generate actionable business reports, and manage SQL data models.",
        location="Pune, MH",
        salary=800000,
        job_type="Full Time",
        skills="SQL, Python, Excel, Tableau"
    )
]


@router.post("/")
def create_job(job: JobCreate):
    jobs.append(job)
    return {
        "message": "Job Created Successfully",
        "job": job
    }


@router.get("/")
def get_jobs():
    return jobs


@router.get("/{job_id}")
def get_job(job_id: int):
    if job_id < 0 or job_id >= len(jobs):
        raise HTTPException(status_code=404, detail="Job not found")

    job = jobs[job_id]

    return {
        "job": {
            "id": job_id,
            "title": job.title,
            "description": job.description,
            "location": job.location,
            "salary": f"₹{job.salary:,}" if isinstance(job.salary, int) else (f"₹{job.salary}" if not str(job.salary).startswith('₹') else job.salary),
            "job_type": job.job_type,
            "company_name": "Demo Company"
        }
    }