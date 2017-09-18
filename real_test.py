from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, Text, Date
from squlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import models
import psycopg2
from config import config

def connect ():
    """Connect to the PostgreSQL database server"""
    conn = create_engine('postgresql+psycopg2://localhost/tracklift')
    try:
        # read the connection parameters
        params = config()

        # connect to the PostgreSQL server
        print ('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        Session = sessionmaker(conn)
        session = Session()
# insert data into the table
        leg_day = Workouts(id=0, Date = 1111-22-33)
        squats = Lifts(id=0, workout=0, warm_up=True, name= "Squat", lift_ord=1,
                workout_ord=1)
        set_rep = Sets(id=0, lift=0, set_count=1, rep_count=1, weight=200, lift_ord =1)
        session.add(leg_day)
        session.add(squats)
        session.add(set_rep)

    # close connection with server
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print (error)
    finally:
        if conn is not None:
            conn.close()
            print ('Database connection closed. Goodbye.')

if __name__ == '__main__':
    connect()
