from pydantic import Field
from pydantic import BaseModel
from typing import Optional


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(max_length=30, min_length=5)
    overview: str = Field(..., min_length=15)
    year: int = Field(..., le=2023)
    rating: float = Field(..., ge=1, le=10)
    category: str = Field(..., min_length=5, max_length=50)

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Title example",
                "overview": "Description",
                "year": 2023,
                "rating": 5.3,
                "category": "example"
            }
        }