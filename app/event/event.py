from collections import OrderedDict
from flask import jsonify, request
from app.event import event_api
from app.models import Event, User, Center, EventSchema
from app import db
from app.exception import ValidationError

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

  event_schema = EventSchema()
  result = event_schema.dump(event).data

  return jsonify({
    'message': 'Event created successfully',
    'events': result
  }), 201

@event_api.route('/events', methods = ['GET'])
def get_all_events():
  all_events = Event.query.all()
  events_schema = EventSchema(many=True)
  result = events_schema.dump(all_events)

  return jsonify({
    'success': 'true',
    'message': 'message retrieved successfully',
    'event': result.data 
  }), 200

@event_api.route('/events/<int:eventId>', methods = ['GET'])
def get_one_event(eventId):
  event = Event.query.get(eventId)

  if not event:
    return jsonify({
      'success': 'false',
      'message': 'Event does not exist'
    }), 404

  event_schema = EventSchema()
  result = event_schema.dump(event)

  return jsonify({
    'success': 'true',
    'message': 'message retrieved successfully',
    'event': result.data 
  }), 200

@event_api.route('/events/<int:eventId>', methods = ['PUT'])
def edit_event(eventId):
  try:
    event = Event.query.get(eventId)

    if not event:
      return jsonify({
        'success': 'false',
        'message': 'Event does not exist'
      }), 404

    if not request.form['event_name'] or not request.form['event_date']:
      pass

    event.event_name = request.form['event_name']
    event.event_date = request.form['event_date']

    db.session.add(event)
    db.session.commit()

    event_schema = EventSchema()
    result = event_schema.dump(event)
    return jsonify({
      'success': 'true',
      'message': 'message retrieved successfully',
      'event': result.data 
    }), 201

  except KeyError as error:
    raise ValidationError('Invalid entries, missing ' + error.args[0])


@event_api.route('/events/<int:eventId>', methods = ['DELETE'])
def delete_event():
  return ''


