from fastapi import APIRouter
from fastapi import HTTPException, Body, Path, Query, status, Depends
from fastapi.responses import HTMLResponse, JSONResponse

from typing import List

from middlewares.jwt import JWTBearer
from schemas.movie_schema import Movie
from data.data import movies

router = APIRouter()


@router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hola</h1>')


@router.get(
    '/movies',
    tags=['movies'],
    response_model=List[Movie],
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())]
)
def get_movies():
    return JSONResponse(status_code=status.HTTP_200_OK, content=movies)


@router.get('/movies/{id}', tags=['movies'], status_code=status.HTTP_200_OK)
def get_movie(id: int = Path(ge=1, le=2000)):
    for i in movies:
        if i["id"] == id:
            return JSONResponse(content=i, status_code=status.HTTP_200_OK)

    return JSONResponse(content=[], status_code=status.HTTP_404_NOT_FOUND)


@router.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str = Query(min_length=5, max_length=15)):
    data = [item for item in movies if item['category'] == category]
    return JSONResponse(content=data)


@router.post(
    '/movies',
    tags=['movies']
)
def create_movie(movie: Movie = Body(...)):
    movies.append(movie.dict())

    return JSONResponse(content={"message": "Se ha registrado la película"})


@router.put("/movies/{id}", tags=['movies'])
def update_movie(id: int, movie: Movie = Body(...)):
    for index, item in enumerate(movies):
        if item['id'] == id:
            movie.id = id
            movies[index].update(movie.dict())
            return JSONResponse(content={"message": "Se ha actualizado la película"})

    raise HTTPException(status_code=404, detail="Movie not found")


@router.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for index, item in enumerate(movies):
        if item['id'] == id:
            del movies[index]
            return JSONResponse(content={"message": "Se ha eliminado la película"})

    raise HTTPException(status_code=404, detail="Movie not found")