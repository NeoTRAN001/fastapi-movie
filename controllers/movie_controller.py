from fastapi import APIRouter
from fastapi import HTTPException, Body, Path
from fastapi.responses import HTMLResponse

from schemas.movie_schema import Movie
from data.data import movies

router = APIRouter()


@router.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hola</h1>')


@router.get('/movies', tags=['movies'])
def get_movies():
    return movies


@router.get('/movies/{id}', tags=['movies'])
def get_movie(id: int = Path(ge=1, le=2000)):
    for i in movies:
        if i["id"] == id:
            return i

    return []


@router.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]


@router.post(
    '/movies',
    tags=['movies']
)
def create_movie(movie: Movie = Body(...)):
    movies.append(movie.dict())

    return movies


@router.put("/movies/{id}", tags=['movies'])
def update_movie(id: int, movie: Movie = Body(...)):
    for index, item in enumerate(movies):
        if item['id'] == id:
            movie.id = id
            movies[index].update(movie.dict())
            return movies

    raise HTTPException(status_code=404, detail="Movie not found")


@router.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for index, item in enumerate(movies):
        if item['id'] == id:
            del movies[index]
            return {'status': 'deleted movie'}

    raise HTTPException(status_code=404, detail="Movie not found")