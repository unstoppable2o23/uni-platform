from fastapi import FastAPI
from app.models import StudentProfile, RecommendationResult
from app.recommender import generate_recommendations
import uvicorn

app = FastAPI(title="Production Uni Platform")

@app.post("/recommend", response_model=list[RecommendationResult])
def recommend(student: StudentProfile):
    return generate_recommendations(student)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)
