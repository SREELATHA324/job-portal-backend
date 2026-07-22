from fastapi import APIRouter
from pydantic import BaseModel
from app.schemas.application import JobApplication

router = APIRouter(
    prefix="/user",
    tags=["User"]
)

users = []
profiles = []
applications = []


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str = "User"


@router.post("/register")
def register_user(user: UserCreate):
    users.append(user)

    return {
        "message": "User Registered Successfully",
        "user": user
    }


@router.get("/users")
def get_users():
    return {
        "users": users
    }


class UserProfile(BaseModel):
    name: str
    email: str
    skills: str
    experience: str
    resume: str


@router.post("/profile")
def create_profile(profile: UserProfile):
    profiles.append(profile)

    return {
        "message": "Profile Created Successfully",
        "profile": profile
    }


@router.get("/profile/{email}")
def get_profile(email: str):

    for profile in profiles:
        if profile.email == email:
            return {
                "profile": profile
            }

    return {
        "message": "Profile not found"
    }


@router.post("/apply")
def apply_job(application: JobApplication):

    application.ats_score = 80
    application.status = "Applied"

    applications.append(application)

    return {
        "message": "Job Applied Successfully",
        "application": application
    }


@router.get("/applications")
def get_applications():
    return {
        "applications": applications
    }