from fastapi import FastAPI
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app:FastAPI):
    # TODO: remove all the prints with the logger
    print("Starting FLUXX-API application")
    yield
    print("Shutting down FLUXX-API application")

app = FastAPI(
    title="My FastAPI App",
    version="0.1.0",
    lifespan=lifespan
)

@app.get("/")
async def root():
    """Root route of the API"""
    return {"message": "Hello billing"}
