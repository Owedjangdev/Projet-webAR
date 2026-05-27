from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.database import Base


class Experience(Base):
    __tablename__ = "experiences"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    experience_id: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    title: Mapped[str] = mapped_column(String(150), nullable=False)
    template: Mapped[str] = mapped_column(String(80), nullable=False)
    status: Mapped[str] = mapped_column(String(30), default="draft")
    place_id: Mapped[int] = mapped_column(ForeignKey("places.id"), nullable=False)

    place = relationship("Place", back_populates="experiences")
    config = relationship("ExperienceConfig", back_populates="experience", uselist=False)
    assets = relationship("Asset", back_populates="experience")
