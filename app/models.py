from pydantic import BaseModel
from typing import List

class StudentProfile(BaseModel):
    student_name: str
    gpa: float
    budget_annual_usd: float
    target_countries: List[str]
    skills: List[str]

class RecommendationResult(BaseModel):
    university_name: str
    fit_score: float
    category: str
