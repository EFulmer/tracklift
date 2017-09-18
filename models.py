import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Text, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import relationship

class Workouts(Base):
    __tablename__ = 'workouts'
    
    id = Column(Integer, primary_key = True)
    day = Column(Date, nullable = False)
    get_pumped = relationship("Lifts", back_populates =  "workouts")

class Lifts(Base):
    __tablename__ = 'lifts'

    id = Column(Integer, primary_key = True)
    workout = Column(Integer, ForeignKey('workouts.id'))
    warm_up = Column(Boolean, nullable = False)
    name = Column(Text, nullable = False)
    lift_ord = Column(Integer, nullable = False)
    workout_ord = Column(Integer, nullable = False)
    
    lifts = relationship("Lifts", back_populates = "get_pumped")
    milk_for_babies = relationship("Sets", back_populates = "lifts")

class Sets(Base):
    __tablename__ = 'sets'

    id = Column(Integer, primary_key = True)
    lift = Column(Integer, ForeignKey('lifts.id'))
    set_count = Column(Integer, nullable = False)
    rep_count = Column(Integer, nullable = False)
    weight = Column(Integer, nullable = False)
    notes = Column(Text, nullable = False)
    lift_ord = Column(Integer, nullable = False)

    sets = relationship("Sets", back_populates = "milk_for_babies")
