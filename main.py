from flask import Flask, request
import re
import psycopg2
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text, Date
from sqlalchemy.orm import sessionmaker
from models import Workouts, Lifts, Sets
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'localhost://tracklift'
# db = SQLAlchemy(app)

db_string = "postgresql+psycopg2://localhost/tracklift"
engine = create_engine(db_string)

Session = sessionmaker(bind = engine)
session = Session()

@app.route('/workouts/<id>/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def workout_query(id):
    if request.method == 'GET':
        for workout in session.query(Workouts):
            return jsonify(id = str(workout.id), day = str(workout.day))

@app.route('/lifts/<id>/', methods = ['GET', 'POST', 'PUT', 'DELETE'])
def lift_query(id):
    if request.method == 'GET':
        for lift in session.query(Lifts):
            return str((lift.name))



@app.route('/date/<date>')
def date_check(date):
    if re.match('\d{4}-\d{1,2}-\d{1,2}', date):
        return 'Date = %s' % date
    else:
        return 'Date invalid, please use "YYYY-MM-DD" format'

if __name__ == '__main__':
    app.run(debug=True)
