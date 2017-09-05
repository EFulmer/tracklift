from flask import Flask, request
app = Flask(__name__)
import re

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

# The next step is to add sets, reps, weight to the lift_type function.
# We want the lift_type function to be a POST only
# We want the date_check to be GET only
# See Slack for what the eventual JSON response will be for lift_type
