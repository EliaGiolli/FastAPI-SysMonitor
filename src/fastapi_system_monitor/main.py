from contextlib import asynccontextmanager

from fastapi import FastAPI

from fastapi_system_monitor.core.database import create_db_and_tables

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


app = FastAPI(title="System Monitor", lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok"}