from pydantic import BaseModel


class PlacePublic(BaseModel):
    name: str
    city: str


class ExperienceConfigPublic(BaseModel):
    message: str
    color: str


class ExperiencePublic(BaseModel):
    experience_id: str
    template: str
    place: PlacePublic
    assets: dict[str, str]
    config: ExperienceConfigPublic


class ExperienceListItem(BaseModel):
    experience_id: str
    title: str
    template: str
    status: str
    place: PlacePublic
