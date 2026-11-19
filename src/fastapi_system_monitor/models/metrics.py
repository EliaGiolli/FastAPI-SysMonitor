from datetime import datetime, timezone

from sqlmodel import Field, Relationship, SQLModel


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class NetworkInterfaceStatBase(SQLModel):
    interface_name: str
    bytes_sent: int
    bytes_recv: int
    packets_sent: int
    packets_recv: int


class SystemSnapshotBase(SQLModel):
    cpu_percent: float
    memory_total: int
    memory_available: int
    memory_percent: float


class SystemSnapshot(SystemSnapshotBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    timestamp: datetime = Field(default_factory=utc_now, index=True)
    interfaces: list["NetworkInterfaceStat"] = Relationship(back_populates="snapshot")


class NetworkInterfaceStat(NetworkInterfaceStatBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    snapshot_id: int = Field(foreign_key="systemsnapshot.id", index=True)
    snapshot: SystemSnapshot | None = Relationship(back_populates="interfaces")