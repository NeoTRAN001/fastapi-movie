import uvicorn

from fastapi import FastAPI

import services.jwt_service
from controllers import movie_controller, auth_controller

app = FastAPI()


def config():
    app.title = 'Movie API REST'
    app.version = '0.0.1'


def routes():
    controllers = [movie_controller, auth_controller]

    for controller in controllers:
        app.include_router(controller.router)


if __name__ == "__main__":
    config()
    routes()
    uvicorn.run(app, host="127.0.0.1", port=8000)
