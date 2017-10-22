from flask import Flask, request
import re
# import psycopg2
import sqlalchemy
from datetime import datetime
from sqlalchemy import create_engine
# from sqlalchemy import Column, String, Integer, ForeignKey, Boolean, Text, Date
from sqlalchemy.orm import sessionmaker
from models import Workouts, Lifts, Sets
# from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
db_string = "postgresql+psycopg2://localhost/tracklift"
engine = create_engine(db_string)

Session = sessionmaker(bind=engine)
session = Session()

@app.route('/workouts/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/workouts/', methods = ['POST'], defaults={'id': None})
def workout_query(id):
    if request.method == 'GET':
        get_result =  session.query(Workouts).filter_by(id=id).first()
        return jsonify({"id":str(get_result.id),"day":str(get_result.day)})
    
    elif request.method == 'DELETE':
        delete_result = session.query(Workouts).filter_by(id=id).first()
        # TODO: add foreign keys
        session.query(Workouts).filter_by(id=id).delete()
        session.commit()
        return jsonify({"id":str(delete_result.id),"day":str(delete_result.day)})

    elif request.method == 'PUT':
        put_result = session.query(Workouts).filter_by(id=id).first()
        update_result = datetime.strptime(request.get_json(force=True)['day'], '%m-%d-%Y')
        new_result = session.query(Workouts) \
                .filter_by(id=id).update({"day":update_result})
        session.commit()
        return jsonify({"id":str(put_result.id),"day":str(put_result.day)})

    elif request.method == 'POST':
        post_result = session.query(Workouts).first()
        new_post = datetime.strptime(request.get_json(force=True)['day'], '%m-%d-%Y')
        post_result = Workouts(day=new_post)
        session.add(post_result)
        session.commit()
        return jsonify({"id":str(post_result.id), "day":str(post_result.day)})

@app.route('/lifts/<id>/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def lift_query(id):
    if request.method == 'GET':
        get_lift = session.query(Lifts).filter_by(id=id).first()
        return jsonify({"id":str(get_lift.id), "workout": str(get_lift.workout)
                , "warm_up":get_lift.warm_up, "name":get_lift.name
                , "lift_ord":str(get_lift.lift_ord), "workout_ord":str(get_lift.workout_ord)})


@app.route('/date/<date>')
def date_check(date):
    if re.match('\d{4}-\d{1,2}-\d{1,2}', date):
        return 'Date = %s' % date
    else:
        return 'Date invalid, please use "YYYY-MM-DD" format'


if __name__ == '__main__':
    app.run(debug=True)
