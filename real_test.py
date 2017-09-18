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

        Session = sessionmaker(db)
        session = Session()
# insert data
        leg_day = Workouts(id=0, Date =  

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print (db_version)

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
