import uvicorn
from fastapi import FastAPI
import logging

from app.MainController import router
from app.RestService import config


app = FastAPI(title=config.title)
app.include_router(router)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    uvicorn.run(app, port=config.port)