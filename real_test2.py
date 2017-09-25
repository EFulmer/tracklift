from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Text, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from models import Workouts, Lifts, Sets
import psycopg2
from config import config

db_string = "postgresql+psycopg2://localhost/tracklift"
db = create_engine(db_string)
# base = declarative_base()

# create db session
Session = sessionmaker(db)
session = Session()

# connect to the PostgreSQL server
print ('Connecting to the PostgreSQL database...')

# create
leg_day = Workouts(id=1, day = '2017-2-3')
squats = Lifts(id=2, workout=0, warm_up=True, name= "Squat", lift_ord=1,
        workout_ord=1)
set_rep = Sets(id=3, lift=0, set_count=1, rep_count=1, weight=200, lift_ord =1)
session.add(leg_day)
session.add(squats)
session.add(set_rep)

# read
workouts = session.query(Workouts)
for workout in workouts:
    print(workout.day)

swole = session.query(Lifts)
for get in swole:
    print(get.name)

huge = session.query(Sets)
for makeme in huge:
    print(makeme.weight)

# update
set_rep.weight = 240
session.commit

updated = session.query(Sets)
for updates in updated:
    print(updates.weight)

# delete
session.delete(set_rep)
session.commit()
