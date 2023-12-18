"""FastAPI"""
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get(path="/")
async def root():
    """Handle root"""
    return {"Hello": "World"}


def start():
    """Launch in watch mode"""
    print("Hello World")
    uvicorn.run(app="portal.main:app", host="0.0.0.0", port=8000, reload=True)
