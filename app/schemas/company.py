from pydantic import BaseModel

class CompanyCreate(BaseModel):
    company_name: str
    location: str
    website: str
    description: str