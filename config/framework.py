from fastapi import FastAPI

app = FastAPI()


def app_config(controllers):
    app.title = 'Movie API REST and MySQL'
    app.version = '0.0.2'

    for controller in controllers:
        app.include_router(controller.router)
