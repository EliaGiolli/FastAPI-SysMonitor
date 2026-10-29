from fastapi import FastAPI

from app.models.network_utils_model import create_db_and_tables

app = FastAPI()

@app.on_event("startup")
def startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"message": "Database e tabelle inizializzati con successo!"}
