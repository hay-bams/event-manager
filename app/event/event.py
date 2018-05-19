from flask import jsonify, request
from app.event import event_api
from app.models import Event, User, Center
from app import db

@event_api.route('/events', methods = ['POST'])
def create_event():
  event = Event()
  token = request.headers['token']
  user_id = event.decode_token(token)
  user = User.query.get(user_id)
  center = Center.query.get(1)

  event.import_data(request.form)
  event.user = user
  event.center = center

  db.session.add(event)
  db.session.commit()

  return jsonify({
    'message': 'Event created successfully'
  })

@event_api.route('/events/<int:eventId>', methods = ['GET', 'PUT'])
def edit_event():
  event= request.get_json()

@event_api.route('/events/<int:eventId>', methods = ['DELETE'])
def delete_event():
  return ''


