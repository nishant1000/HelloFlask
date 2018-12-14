from app import app, db
from flask import request, json
from models.bus_location import BusLocation


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/device_location', methods=['POST'])
def device_location():
    params = request.json
    latitude = params['latitude']
    longitude = params['longitude']
    device_id = params['device_id']
    b = BusLocation.query.filter_by(device_id=10).first()
    if(b is None):
        b = BusLocation(device_id, latitude, longitude)
    else:
        b.latitude = latitude
        b.longitude = longitude
    db.session.add(b)
    db.session.commit()

    response = app.response_class(
        status=200,
        mimetype='application/json')
    return response
