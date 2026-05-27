from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.experience import Experience
from app.schemas.experience import ExperienceListItem, ExperiencePublic


router = APIRouter()


@router.get("/experiences", response_model=list[ExperienceListItem])
def list_experiences(db: Session = Depends(get_db)):
    experiences = db.query(Experience).all()

    return [
        {
            "experience_id": experience.experience_id,
            "title": experience.title,
            "template": experience.template,
            "status": experience.status,
            "place": {
                "name": experience.place.name,
                "city": experience.place.city,
            },
        }
        for experience in experiences
    ]


@router.get("/experience/{experience_id}", response_model=ExperiencePublic)
def get_experience(experience_id: str, db: Session = Depends(get_db)):
    experience = (
        db.query(Experience)
        .filter(Experience.experience_id == experience_id)
        .first()
    )

    if experience is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Experience introuvable",
        )

    assets = {asset.type: asset.url for asset in experience.assets}

    return {
        "experience_id": experience.experience_id,
        "template": experience.template,
        "place": {
            "name": experience.place.name,
            "city": experience.place.city,
        },
        "assets": assets,
        "config": {
            "message": experience.config.message,
            "color": experience.config.color,
        },
    }
