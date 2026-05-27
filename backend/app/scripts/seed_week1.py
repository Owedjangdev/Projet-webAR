from app.db.database import SessionLocal
from app.models.asset import Asset
from app.models.experience import Experience
from app.models.experience_config import ExperienceConfig
from app.models.place import Place


def main():
    db = SessionLocal()
    try:
        existing = (
            db.query(Experience)
            .filter(Experience.experience_id == "exp_001")
            .first()
        )
        if existing:
            print("Experience exp_001 existe deja.")
            return

        place = Place(
            name="Restaurant Le Palmier",
            type="restaurant",
            city="Cotonou",
            address="Cotonou, Benin",
            description="Lieu de demonstration pour la premiere semaine.",
        )
        db.add(place)
        db.flush()

        experience = Experience(
            experience_id="exp_001",
            title="Selfie Souvenir au Palmier",
            template="selfie_ar",
            status="published",
            place_id=place.id,
        )
        db.add(experience)
        db.flush()

        config = ExperienceConfig(
            experience_id=experience.id,
            message="Souvenir au Palmier",
            color="#FFAA00",
            options={},
        )
        db.add(config)

        db.add_all(
            [
                Asset(
                    experience_id=experience.id,
                    type="overlay_image",
                    url="https://example.com/assets/palmier-overlay.png",
                    alt_text="Overlay decoratif du Palmier",
                ),
                Asset(
                    experience_id=experience.id,
                    type="logo",
                    url="https://example.com/assets/palmier-logo.png",
                    alt_text="Logo du restaurant Le Palmier",
                ),
            ]
        )

        db.commit()
        print("Donnees de test semaine 1 inserees avec succes.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
