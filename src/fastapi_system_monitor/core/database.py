from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel

from fastapi_system_monitor.models import metrics


engine = create_engine('sqlite:///prova.db', echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]