from pydantic import BaseModel
from typing import Union, Optional

class JobCreate(BaseModel):
    title: str
    description: str
    location: str
    salary: Union[int, str] = 0
    job_type: str
    skills: Optional[str] = ""