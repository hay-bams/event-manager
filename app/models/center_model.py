from app import db
from datetime import datetime
from app.exception import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash


class Center(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    center_name = db.Column(db.String(64), index=True)
    center_location = db.Column(db.String(100), index=True)
    center_capacity = db.Column(db.Integer, index=True)
    center_status = db.Column(db.Boolean(), nullable=False, server_default='1')
    event = db.relationship(
      'Event',
      backref='center',
      lazy='dynamic')

    def is_available(self, date):
        pass

    def __repr__(self):
        return '<Center {}>'.format(self.center_name)