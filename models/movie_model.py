from pydantic import Field
from pydantic import BaseModel


class Movie(BaseModel):
    id: int = Field(...)
    title: str = Field(...)
    overview: str = Field(...)
    year: int = Field(...)
    rating: float = Field(...)
    category: str = Field(...)
