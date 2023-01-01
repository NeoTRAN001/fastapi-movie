import uvicorn
from fastapi import FastAPI
from fastapi import Body
from fastapi import HTTPException
from fastapi.responses import HTMLResponse

from models.movie_model import Movie

app = FastAPI()
app.title = 'Movie API REST'
app.version = '0.0.1'

movies: [Movie] = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar 2",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hola</h1>')


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies


@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for i in movies:
        if i["id"] == id:
            return i

    return []


@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item['category'] == category]


@app.post(
    '/movies',
    tags=['movies']
)
def create_movie(movie: Movie = Body(...)):
    movies.append(movie.dict())

    return movies


@app.put("/movies", tags=['movies'])
def update_movie(movie: Movie = Body(...)):
    for index, item in enumerate(movies):
        if item['id'] == movie.id:
            movies[index].update(movie.dict())
            return movies

    raise HTTPException(status_code=404, detail="Movie not found")


@app.delete('/movies/{id}', tags=['movies'])
def delete_movie(id: int):
    for index, item in enumerate(movies):
        if item['id'] == id:
            del movies[index]
            return {'status': 'deleted movie'}

    raise HTTPException(status_code=404, detail="Movie not found")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
