import uvicorn

from fastapi import FastAPI
from controllers import movie_controller

app = FastAPI()


def config():
    app.title = 'Movie API REST'
    app.version = '0.0.1'


def routes():
    app.include_router(movie_controller.router)


if __name__ == "__main__":
    config()
    routes()
    uvicorn.run(app, host="127.0.0.1", port=8000)
