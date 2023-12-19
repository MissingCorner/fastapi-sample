"""FastAPI"""
from fastapi import FastAPI

from .modules.core.router import router as core_router
from .modules.user.router import router as user_router

app = FastAPI()


app.include_router(core_router)
app.include_router(user_router)
