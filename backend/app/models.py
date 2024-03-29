import datetime
from pydantic import BaseModel
from sqlmodel import Relationship, SQLModel, Field


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    username: str = Field(nullable=False)
    password: str = Field(nullable=False)


class Token(BaseModel):
    type: str
    token: str


class Device(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str | None = Field(index=True)
    device_data: list["DeviceData"] = Relationship(back_populates="device")


class DeviceData(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    parameter: str | None
    timestamp: datetime.datetime | None
    value: str | None
    type: str | None
    device_id: int | None = Field(default=None, foreign_key="device.id")
    device: Device | None = Relationship(back_populates="device_data")
