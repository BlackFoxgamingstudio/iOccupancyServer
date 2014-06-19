from flask import Flask, render_template, request, jsonify
from model import  Beacons, db, Tests,TrainingResult
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import  Api
from resources import *
#import bluetooth_server
import thread




# Initialize the Flask application

app = Flask(__name__)


api = Api(app)
api.add_resource(deviceMinimalLogic, '/ibeacon/<string:device>')
api.add_resource(beaconMinimalLogic, '/ibeacon/<string:device>/<string:beacon>')
api.add_resource(deviceFullLogic, '/ibeaconserver/<string:device>')
api.add_resource(testBasic, '/ibeacon/test_basic')
api.add_resource(login,'/ibeacon/login')
api.add_resource(training,'/ibeacon/training')
api.add_resource(testLearning,'/ibeacon/testLearning')
api.add_resource(testClientFinal,'/ibeacon/testClient')


@app.before_first_request
def setup():
    app.debug = True





@app.route('/')
def index():

  # Render template
  locations = db.session.query(Beacons).all()
  return render_template('request.html', data=locations)

@app.route('/location')
def location():

  # Render template
  local = db.session.query(Locations).all()
  return render_template('locations.html', data=local)

@app.route('/tests')
def tests():
  # Render template
  local = db.session.query(Tests).all()
  return render_template('tests.html', data=local)


def setup():
  learning_machine.load_data()

#def launch_bluetooth_server():
 # bluetooth_server.runServer()

# Run

if __name__ == '__main__':
    setup()
   # thread.start_new_thread( launch_bluetooth_server,())
    app.run(
        host = "0.0.0.0",
        port = 80
    )



