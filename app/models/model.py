# from app import db
# from datetime import datetime
# from app.exception import ValidationError
# from werkzeug.security import generate_password_hash, check_password_hash

# class User(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   username = db.Column(db.String(64), index=True, unique=True, nullable=False)
#   password = db.Column(db.String(64), index=True, nullable=False)
#   events = db.relationship(
#     'Event',
#     backref='user',
#     lazy= 'dynamic')

#   def set_password_hash(self, password):
#     self.password = generate_password_hash(password)

#   def verify_password(self, password):
#     password_hash = self.password
#     return check_password_hash(password_hash, password)

#   def import_data(self, data):
#     try:
#       for field in ['username', 'password']:
#         setattr(self, field, data[field])
#     except KeyError as e:
#       raise ValidationError('Invalid user, missing ' + e.args[0])
#     return self

#   def __repr__(self):
#     return '<User {}>'.format(self.username)

# class Center(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   center_name = db.Column(db.String(64), index=True)
#   center_location = db.Column(db.String(100), index=True)
#   center_capacity = db.Column(db.Integer, index=True)
#   center_status = db.Column(db.Boolean(), nullable=False, server_default='1')
#   event = db.relationship(
#     'Event',
#     backref='center',
#     lazy='dynamic')

#   def is_available(self, date):
#     pass

#   def __repr__(self):
#     return '<Center {}>'.format(self.center_name)

# class Event(db.Model):
#   id = db.Column(db.Integer, primary_key=True)
#   event_name = db.Column(db.String(64), index=True)
#   event_date = db.Column(db.Date, nullable=False)
#   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#   center_id = db.Column(db.Integer, db.ForeignKey('center.id'))

#   def __repr__(self):
#     return '<Event {}>'.format(self.event_name)
