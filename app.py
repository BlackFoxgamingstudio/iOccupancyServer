from flask import Flask, render_template, request, jsonify
from model import  Beacons, db
from flask_sqlalchemy import SQLAlchemy
from flask.ext.restful import  Api
from resources import *



# Initialize the Flask application

app = Flask(__name__)


api = Api(app)
api.add_resource(Device, '/ibeacon/<string:device>')
api.add_resource(Ibeacon, '/ibeacon/<string:device>/<string:beacon>')
api.add_resource(DeviceServer, '/ibeaconserver/<string:device>')
api.add_resource(IbeaconServer, '/ibeaconserver/<string:device>/<string:beacon>')


@app.before_first_request
def setup():
    app.debug = True





@app.route('/')
def index():

  # Render template
  locations = db.session.query(Beacons).all()
  return render_template('request.html', data=locations)






# Run
if __name__ == '__main__':
    app.run(
        host = "0.0.0.0",
        port = 80
    )
