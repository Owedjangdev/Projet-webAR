from sqlalchemy import ForeignKey, Integer, JSON, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class ExperienceConfig(Base):
    __tablename__ = "experience_configs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    experience_id: Mapped[int] = mapped_column(ForeignKey("experiences.id"), unique=True)
    message: Mapped[str] = mapped_column(String(255), nullable=False)
    color: Mapped[str] = mapped_column(String(20), default="#FFAA00")
    options: Mapped[dict | None] = mapped_column(JSON, nullable=True)

    experience = relationship("Experience", back_populates="config")
