from datetime import datetime

from fastapi_system_monitor.models.metrics import (
    NetworkInterfaceStatBase,
    SystemSnapshotBase,
)


class NetworkInterfaceStatPublic(NetworkInterfaceStatBase):
    # without 'None' we're telling Python that the id is mandatory
    id: int


class SystemSnapshotPublic(SystemSnapshotBase):
    id: int
    timestamp: datetime
    # the nested interface tells us that the response will be a JSON with a list of interfaces
    interfaces: list[NetworkInterfaceStatPublic]