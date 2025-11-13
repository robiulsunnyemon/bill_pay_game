from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.bill_pay_game.database.db import initialize_database, close_database
from src.bill_pay_game.session.routers.session import router as session_router
from src.bill_pay_game.session_group.routers.session_group import router as session_group_router

@asynccontextmanager
async def lifespan_context(_: FastAPI):
    await initialize_database()
    yield
    await close_database()

app = FastAPI(
    prefix="/api",
    title="Bill Pay Game",
    description="Bill Pay Game API",
    version="1.0.0",
    lifespan=lifespan_context,
)

@app.get("/")
async def root():
    return {"message": "Welcome to Bill Pay Game API!"}

app.include_router(session_router)
app.include_router(session_group_router)
