from sqlalchemy import Column, Integer, String, Time, TEXT, DateTime, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import Base
from sqlalchemy.sql import func
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    password = Column(String)
    email = Column(String)
    is_admin = Column(Boolean, default=False)
    date_created = Column(DateTime, default=datetime.utcnow())
    reset_pass = relationship('ResetPass', back_populates='user')

class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    abbreviation = Column(String)
    continent = Column(String)


class Holidays(Base):
    __tablename__ = "holidays"
    id = Column(Integer, primary_key=True, index=True)
    country_id = Column(Integer, ForeignKey('countries.id'))
    Holiday_date = Column(DateTime(timezone=True))
    holiday_name = Column(String)
    holiday_type = Column(String)
    comments = Column(String)


