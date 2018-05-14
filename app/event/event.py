from flask import jsonify, request
from app.event import event_api
from app.models import Event


@event_api.route('/events', methods = ['GET', 'POST'])
def create_event(self):
  event = request.get_json()
  print(event)

@event_api.route('/events/<int:eventId>', methods = ['GET', 'PUT'])
def edit_event(self):
  event= request.get_json()

@event_api.route('/events/<int:eventId>', methods = ['DELETE'])
def delete_event(self):
  return ''


