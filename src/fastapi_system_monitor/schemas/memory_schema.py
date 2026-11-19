from pydantic import BaseModel

class MemorySchema(BaseModel):
    total: int
    available: int
    percent: float

