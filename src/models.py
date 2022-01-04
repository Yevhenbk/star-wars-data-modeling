import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key = True)
    favourites_id = Column(Integer, ForeignKey("favourites.id"))
    have_favourites = relationship("Favourites", back_populates="favourites", uselist=False)

    Username = Column(String(10), unique = True)
    Email = Column(String(25), unique=True, nullable=False)



class Favourites(Base):
    __tablename__ = 'favourites'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("user.id"))
    have_user = relationship("User")


class People(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key = True)
    favourites_id = Column(Integer, ForeignKey("favourites.id"))
    have_favourites = relationship("favourites")

    name = Column(String(30), unique=False, nullable=False)
    height = Column(Integer(5), unique=False, nullable=False)
    mass = Column(Integer(5), unique=False, nullable=False)
    hair_color = Column(String(12), unique=False, nullable=False)
    skin_color = Column(String(12), unique=False, nullable=False)
    eye_color = Column(String(12), unique=False, nullable=False)
    birth_year = Column(Integer(4), unique=False, nullable=False)
    gender = Column(String(10), unique=False, nullable=False)
    homeworld = Column(String(25), unique=False, nullable=False)
    species = Column(String(25), unique=False, nullable=False)
    vehicles = Column(String(25), unique=False, nullable=False)
    starships = Column(String(25), unique=False, nullable=False)
    created = Column(String(25), unique=False, nullable=False)
    edited = Column(String(25), unique=False, nullable=False)
    url = Column(String(200), unique=False, nullable=False)


class Vehicles(Base):
    __tablename__ = 'vehicles'

    id = Column(Integer, primary_key = True)
    favourites_id = Column(Integer, ForeignKey("favourites.id"))
    have_favourites = relationship("favourites")

    name = Column(String(30), unique=False, nullable=False)
    model = Column(String(40), unique=False, nullable=False)
    manufacturer = Column(String(30), unique=False, nullable=False)
    cost_in_credits = Column(Integer(20), unique=False, nullable=False)
    length = Column(Integer(4), unique=False, nullable=False)
    max_atmosphering_speed = Column(String(10), unique=False, nullable=False)
    crew = Column(String(100), unique=False, nullable=False)
    passengers = Column(String(200), unique=False, nullable=False)
    cargo_capacity = Column(String(20), unique=False, nullable=False)
    consumables = Column(String(50), unique=False, nullable=False)
    vehicle_class = Column(String(20), unique=False, nullable=False)
    pilots = Column(String(100), unique=False, nullable=False)
    created = Column(String(25), unique=False, nullable=False)
    edited = Column(String(25), unique=False, nullable=False)
    url = Column(String(200), unique=False, nullable=False)

class Planets(Base):
    __tablename__ = 'planets'

    id = Column(Integer, primary_key = True)
    favourites_id = Column(Integer, ForeignKey("favourites.id"))
    have_favourites = relationship("favourites")

    name = Column(String(30), unique=False, nullable=False)
    height = Column(Integer(5), unique=False, nullable=False)
    mass = Column(Integer(5), unique=False, nullable=False)
    hair_color = Column(String(12), unique=False, nullable=False)
    skin_color = Column(String(12), unique=False, nullable=False)
    eye_color = Column(String(12), unique=False, nullable=False)
    birth_year = Column(Integer(10), unique=False, nullable=False)
    gender = Column(String(20), unique=False, nullable=False)
    homeworld = Column(String(30), unique=False, nullable=False)
    species = Column(String(50), unique=False, nullable=False)
    vehicles = Column(String(100), unique=False, nullable=False)
    starships = Column(String(100), unique=False, nullable=False)
    created = Column(String(25), unique=False, nullable=False)
    edited = Column(String(25), unique=False, nullable=False)
    url = Column(String(200), unique=False, nullable=False)




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')