import os
from app import db
from datetime import datetime
from app.exception import ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.model_operations import ModelOperations

class Event(db.Model, ModelOperations):
  id = db.Column(db.Integer, primary_key=True)
  event_name = db.Column(db.String(64), index=True)
  event_date = db.Column(db.Date, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
  center_id = db.Column(db.Integer, db.ForeignKey('center.id'))

  def __repr__(self):
    return '<Event {}>'.format(self.event_name)