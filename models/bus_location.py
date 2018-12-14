from app import db


class BusLocation(db.Model):
    __tablename__ = 'bus_locations'
    extend_existing = True

    device_id = db.Column(db.Integer,  primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, device_id, latitude,longitude):
        self.device_id = device_id
        self.latitude = latitude
        self.longitude = longitude
