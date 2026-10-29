from fastapi import FastAPI
from contextlib import asynccontextmanager

from app.core.database import create_db_and_tables

PORT = 8000
@asynccontextmanager
async def lifespan(app: FastAPI):
    try:
        create_db_and_tables()
        print(f"The server is running on port {PORT}")
        yield
    except Exception as e:
        raise RuntimeError(f"Critic error during bootstrapping the application: {e}")

app = FastAPI(lifespan=lifespan)



@app.get("/")
def read_root():
    return {"message": "Database e tabelle inizializzati con successo!"}
