import datetime
from typing import Annotated
from sqlmodel import Field, SQLModel, Session, create_engine, select
from fastapi import Depends, FastAPI, HTTPException, Query

class NetworkUtilsModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cpu: float | None = None
    memory: float | None = None
    timestamp: datetime.datetime | None = None


engine = create_engine('sqlite:///sysmonitor.db', echo=False)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]