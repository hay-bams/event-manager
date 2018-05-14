from app import db
from datetime import datetime
from app.exception import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash

user_event = db.Table(
  'user_event',
  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
  db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

user_center = db.Table(
  'user_center',
  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
  db.Column('center_id', db.Integer, db.ForeignKey('center.id'))
)

center_event = db.Table(
  'center_event',
  db.Column('center_id', db.Integer, db.ForeignKey('center.id')),
  db.Column('event_id', db.Integer, db.ForeignKey('event.id'))
)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True, nullable=False)
  password = db.Column(db.String(64), index=True, nullable=False)
  centers = db.relationship(
    'Center', 
    secondary=user_center, 
    backref=db.backref('user',
    lazy='dynamic'), lazy='dynamic')
  events = db.relationship(
    'Event',
    secondary=user_event,
    backref=db.backref('user',
    lazy= 'dynamic'), lazy='dynamic')

  def set_password_hash(self, password):
    self.password = generate_password_hash(password)

  def verify_password(self, password):
    password_hash = self.password
    return check_password_hash(password_hash, password)

  def import_data(self, data):
    try:
      for field in ['username', 'password']:
        setattr(self, field, data[field])
    except KeyError as e:
      raise ValidationError('Invalid user, missing ' + e.args[0])
    return self


  def __repr__(self):
    return '<User {}>'.format(self.username)

class Center(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  center_name = db.Column(db.String(64), index=True)
  center_location = db.Column(db.String(100), index=True)
  center_capacity = db.Column(db.Integer, index=True)
  center_status = db.Column(db.Boolean(), nullable=False, server_default='1')
  event = db.relationship(
    'Event',
    secondary=center_event,
    backref=db.backref('center',
    lazy='dynamic'), lazy='dynamic')

  def __repr__(self):
    return '<Center {}>'.format(self.center_name)

class Event(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  event_name = db.Column(db.String(64), index=True)
  event_date = db.Column(db.Date, nullable=False)

  def __repr__(self):
    return '<Event {}>'.format(self.event_name)
