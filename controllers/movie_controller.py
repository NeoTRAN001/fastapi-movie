from fastapi import APIRouter
from fastapi import HTTPException, Body, Path, Query, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from typing import List

from middlewares.jwt import JWTBearer
from config.database import Session
from models.movie_model import MovieModel
from schemas.movie_schema import Movie
from data.data import movies

router = APIRouter()


@router.get(
    '/movies',
    tags=['movies'],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())]
)
def get_movies():
    db = Session()
    result = db.query(MovieModel).all()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@router.get('/movies/{id}', tags=['movies'], status_code=status.HTTP_200_OK)
def get_movie(id: int = Path(ge=1, le=2000)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        return JSONResponse(content=[], status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    db = Session()
    result = db.query(MovieModel).filter(MovieModel.category == category).first()

    if not result:
        return JSONResponse(content=[], status_code=status.HTTP_404_NOT_FOUND)

    return JSONResponse(content=jsonable_encoder(result), status_code=status.HTTP_200_OK)


@router.post('/movies', tags=['movies'])
def create_movie(movie: Movie = Body(...)):
    db = Session()
    new_movie = MovieModel(**movie.dict())

    db.add(new_movie)
    db.commit()

    return JSONResponse(content={"message": "Se ha registrado la película"})


@router.put("/movies/{id}", tags=['movies'])
def update_movie(id: int, movie: Movie = Body(...)):
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")

    result.title = movie.title
    result.category = movie.category
    result.overview = movie.overview
    result.year = movie.year
    result.rating = movie.rating

    db.commit()

    return JSONResponse(content={"message": "Se ha actualizado la película"})


@router.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    db = Session()
    result: MovieModel = db.query(MovieModel).filter(MovieModel.id == id).first()

    if not result:
        raise HTTPException(status_code=404, detail="Movie not found")

    db.delete(result)
    db.commit()
    
    return JSONResponse(content={"message": "Se ha eliminado la película"})
