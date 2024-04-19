from enum import Enum
from typing import List
from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import (
    MappedAsDataclass,
    DeclarativeBase,
    mapped_column,
    relationship,
    Mapped,
)

from app.database.models.mixins import Timestamp


class Role(Enum):
    ADMINISTRATOR = 1
    USER = 2


class Base(Timestamp, MappedAsDataclass, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50), unique=True)
    role: Mapped[Role]

    city_id: Mapped[int] = mapped_column(ForeignKey("city.id"))
    city: Mapped["City"] = relationship(back_populates="user")


class City(Base):
    __tablename__ = "city"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str] = mapped_column(String(100))
    zip: Mapped[str] = mapped_column(String(10))

    country_id: Mapped[int] = mapped_column(ForeignKey("country.id"))
    country: Mapped["Country"] = relationship(back_populates="city")


class Country(Base):
    __tablename__ = "country"

    id: Mapped[int] = mapped_column(primary_key=True, init=False)
    name: Mapped[str]

    cities: Mapped[List[City]] = relationship(back_populates="country")
