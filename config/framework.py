from fastapi import FastAPI
from middlewares.error_handler import ErrorHandler

app = FastAPI()


def app_config(controllers):
    app.title = 'Movie API REST and MySQL'
    app.version = '0.0.2'

    app.add_middleware(ErrorHandler)

    for controller in controllers:
        app.include_router(controller.router)
