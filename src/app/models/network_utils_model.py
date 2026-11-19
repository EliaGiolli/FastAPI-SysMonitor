import datetime
from sqlmodel import Field, SQLModel

# Pydantic Schemas
from app.schemas.memory_schema import MemorySchema
from app.schemas.pc_interfaces import PcInterfaces

# SQLModel extends Pydantic's BaseModel
class NetworkUtilsModel(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    cpu: float | None = None
    memory: MemorySchema | None = None
    timestamp: datetime.datetime | None = None
    pc_interfaces: PcInterfaces | None = None
