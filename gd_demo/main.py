# from typing import Annotated
import fastapi
import fastapi.staticfiles

from common.log import default_logger
from api import gd_router

logger = default_logger(__name__)


def create_app():
    app = fastapi.FastAPI()
    app.include_router(gd_router.router, prefix='/files')
    return app


app = create_app()


@app.get('/')
def root():
    return {"message": "Hello World"}
