from flask import Flask, request
app = Flask(__name__)
import re
import psycopg
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text, Date
from sqlalchemy.orm import sessionmaker
from models import Workouts, Lifts, Sets

db_string = "postgresql+psycopg2://localhost/tracklift"
db = create_engine(db_string)

Session = sessionmaker(db)
session = Session()

@app.route('/lift/<lift>', methods = ['GET', 'POST'])
def lift_type(lift):
    if request.method == 'POST':
        return success_post
    else:
        return 'Lift = %s' % lift

@app.route('/date/<date>')
def date_check(date):
    if re.match('\d{4}-\d{1,2}-\d{1,2}', date):
        return 'Date = %s' % date
    else:
        return 'Date invalid, please use "YYYY-MM-DD" format'


