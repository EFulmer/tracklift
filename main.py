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
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# DB URL + dialect (postgresql) and driver (psycopg2)
db_string = "postgresql+psycopg2://localhost/tracklift"
# initialize engine to pass to Session object
engine = create_engine(db_string)

# create a global session class bound to the engine above
Session = sessionmaker(bind=engine)
# individual session for use within this app
session = Session()

# use of dual @app.route to avoid having to build POST into its own function
@app.route('/workouts/<int:id>/', methods=['GET', 'PUT', 'DELETE'])
@app.route('/workouts/', methods = ['POST'], defaults={'id': None})
def workout_query(id):

    """routes for queries that require use of the Workouts table"""

    # if the API request is GET, return a JSON containing the id and day 
    # for the <id> specified in the url
    if request.method == 'GET':
        get_result =  session.query(Workouts).filter_by(id=id).first()
        if not get_result:
            result = jsonify({"error":"No workout with id {} found".format(id)})
            result.error_code = 400
        else: result = jsonify({"id":str(get_result.id),"day":str(get_result.day)})
        return result


    # if the API request is DELETE, delete all records associated with
    # the <id> specificed in the url, and return a JSON containing the original result
    elif request.method == 'DELETE':
        delete_result = session.query(Workouts).filter_by(id=id).first()
        session.delete(delete_result)
        session.commit()
        return jsonify({"id":str(delete_result.id),"day":str(delete_result.day)})

    # if the API request is PUT, update the record associated with the 
    # <id> specified in the URL (converting request JSON to datetime) and 
    # return a JSON containing the updated result.
    elif request.method == 'PUT':
        put_result = session.query(Workouts).filter_by(id=id).first()
        update_result = datetime.strptime(request.get_json(force=True)['day'], '%m-%d-%Y')
        new_result = session.query(Workouts).filter_by(id=id).update({"day":update_result})
        session.commit()
        return jsonify({"id":str(put_result.id),"day":str(put_result.day)})

    # if the API request is POST, create a new record in the database using 
    # the date entered by the user (converting the request JSON to datetime)
    # and return a JSON containing the new record
    elif request.method == 'POST':
        post_result = session.query(Workouts).first()
        new_post = datetime.strptime(request.get_json(force=True)['day'], '%m-%d-%Y')
        post_result = Workouts(day=new_post)
        session.add(post_result)
        session.commit()
        return jsonify({"id":str(post_result.id), "day":str(post_result.day)})
    
#    elif type(id) is not int:
#        return jsonify({"error":"400 Bad Request"})

@app.route('/lifts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
# @app.route('/lifts/<int:workout_id'/>, methods=['GET']
def lift_query(id):
    if request.method == 'GET':
        get_lift = session.query(Lifts).filter_by(id=id).first()
        if not get_lift:
            lift_error = jsonify({"error":"No Lift with id {} found.".format(id)})
            lift_error.error_code= 400
        else: lift_result = jsonify({"id":str(get_lift.id), "workout":str(get_lift.workout)
                , "warm_up":get_lift.warm_up, "name":get_lift.name
                , "lift_ord":str(get_lift.lift_ord)})
        return lift_result
        
        #TODO add workout_ord when DB is updated
    elif request.method == 'DELETE':
        delete_lift = session.query(Lifts).filter_by(id=id).first()
        session.query(Lifts).filter_by(id=id).delete()
        session.commit()
        return jsonify({"id":str(delete_lift.id), "workout":str(delete_lift.workout)
                , "warm_up":delete_lift.warm_up, "name":delete_lift.name
                , "lift_ord":str(delete_lift.lift_ord)})

    elif request.method == 'PUT':
        put_lift = session.query(Lifts).filter_by(id=id).first()
        lift_req = request.get_json(force=True)
        updated_lifts = session.query(Lifts) \
                .filter_by(id=id).update(lift_req)
        session.commit()
        return jsonify({"id":str(put_lift.id), "workout":str(put_lift.workout)
                , "warm_up":put_lift.warm_up, "name":put_lift.name
                , "lift_ord":str(put_lift.lift_ord)})
    elif request.method == 'POST':
        post_lift = session.query(Lifts).first()
        new_lift = request.get_json(force=True)
        lift_result = Lifts(workout=new_lift["workout"], warm_up=new_lift["warm_up"] \
                , name=new_lift["name"], lift_ord=new_lift["lift_ord"])
        session.add(lift_result)
        session.commit()
        return jsonify({"id":str(lift_result.id), "workout":str(lift_result.workout)
                , "warm_up":lift_result.warm_up, "name":lift_result.name
                , "lift_ord":str(lift_result.lift_ord)})

@app.route('/workouts/lifts/<int:workout>/', methods=['GET'])
def lift_from_workout(workout):
    if request.method == 'GET':
        lifts = session.query(Lifts).filter_by(workout=workout).all()
        return jsonify({'lifts':list(map(Lifts.as_dict,lifts))})


@app.route('/sets/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/sets/', methods=['POST'], defaults={'id':None})
def sets_query(id):
    if request.method == 'GET':
        get_sets = session.query(Sets).filter_by(id=id).first()
        if not get_sets:
            set_error = jsonify({"Error":"No sets with id {} found".format(id)})
            set_error.error_code = 400
        else: set_error = jsonify({"id":str(get_sets.id), "lift":str(get_sets.lift)
                , "set_ord":str(get_sets.set_ord), "set_count":str(get_sets.set_count)
                , "rep_count":str(get_sets.rep_count), "weight":str(get_sets.weight)
                , "warm_up":get_sets.warm_up, "notes":get_sets.notes})
        return set_error

    
    elif request.method == 'DELETE':
        delete_set = session.query(Sets).filter_by(id=id).first()
        session.query(Sets).filter_by(id=id).delete()
        session.commit()
        return jsonify({"id":str(delete_set.id), "lift":str(delete_set.lift)
                , "set_ord":str(delete_set.set_ord), "set_count":str(delete_set.set_count)
                , "rep_count":str(delete_set.rep_count), "weight":str(delete_set.weight)
                , "warm_up":delete_set.warm_up, "notes":delete_set.notes})

    elif request.method == 'PUT':
        put_set = session.query(Sets).filter_by(id=id).first()
        set_req = request.get_json(force=True)
        updated_sets = session.query(Sets) \
                .filter_by(id=id).update(set_req)
        session.commit()
        return jsonify({"id":str(put_set.id), "lift":str(put_set.lift)
                , "set_ord":str(put_set.set_ord), "set_count":str(put_set.set_count)
                , "rep_count":str(put_set.rep_count), "weight":str(put_set.weight)
                , "warm_up":put_set.warm_up, "notes":put_set.notes})

    elif request.method == 'POST':
        post_set = session.query(Sets).first()
        new_set = request.get_json(force=True)
        set_result = Sets(lift=new_set["lift"], set_ord=new_set["set_ord"] \
                , set_count=new_set["set_count"], rep_count=new_set["rep_count"] \
                , weight=new_set["weight"], warm_up=new_set["warm_up"] \
                , notes=new_set["notes"])
        session.add(set_result)
        session.commit
        return jsonify({"id":str(set_result.id), "lift":str(set_result.lift)
                , "set_ord":str(set_result.set_ord), "set_count":str(set_result.set_count)
                , "rep_count":str(set_result.rep_count), "weight":str(set_result.weight)
                , "warm_up":set_result.warm_up, "notes":set_result.notes})

@app.route('/lifts/sets/<int:lift>/', methods=['GET'])
def sets_from_lift(lift):
    if request.method == 'GET':
        sets = session.query(Sets).filter_by(lift=lift).all()
        return jsonify({'sets':list(map(Sets.sets_as_dict, sets))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
