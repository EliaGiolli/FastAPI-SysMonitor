from pydantic import BaseModel
from sqlmodel import Field

class PcInterfaces(BaseModel):
    interface_name: str = Field(default=None, nullable=True)
    bytes_sent: float = Field(default=None, nullable=True)
    bytes_recv: float = Field(default=None, nullable=True)
    packets_sent: float = Field(default=None, nullable=True)
    packets_recv: float = Field(default=None, nullable=True)