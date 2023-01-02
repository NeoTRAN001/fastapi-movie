import uvicorn

from config.framework import app, app_config
from config.database import db_config
from controllers import movie_controller, auth_controller

routes_controller = [movie_controller, auth_controller]


if __name__ == "__main__":
    app_config(routes_controller)
    db_config()

    uvicorn.run(app, host="127.0.0.1", port=8000)
