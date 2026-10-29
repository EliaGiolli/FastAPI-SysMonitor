from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session, SQLModel

engine = create_engine('sqlite:///sysmonitor.db', echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]