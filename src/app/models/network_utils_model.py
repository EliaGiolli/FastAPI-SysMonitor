import datetime
from sqlmodel import Field, SQLModel

# SQLModel extends Pydantic's BaseModel
class NetworkUtilsModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cpu: float | None = None
    memory: float | None = None
    timestamp: datetime.datetime | None = None

