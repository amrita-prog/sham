import logging
logging.basicConfig(level=logging.DEBUG)

from fastapi import FastAPI
from sh.teacher_routes import router as teacher_router

app = FastAPI()
app.include_router(teacher_router)


