from collections import OrderedDict
from flask import jsonify, request
from app.event import event_api
from app.models import Event, User, Center, EventSchema
from app import db
from app.exception import ValidationError
from flask_restful import Resource


class Events(Resource):
    def get(self):
        all_events = Event.query.all()
        events_schema = EventSchema(many=True)
        result = events_schema.dump(all_events)

        return {
            'success': 'true',
            'message': 'message retrieved successfully',
            'event': result.data
        }, 200

    def post(self):
        event = Event()
        
        if 'token' not in request.headers:
            return {
                'message': 'User not signed in'
            }, 401
            
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

        return {
            'message': 'Event created successfully',
            'events': result
        }, 201


class SingleEvent(Resource):
    def get(self, eventId):
        event = Event.query.get(eventId)

        if not event:
            return {
                'success': 'false',
                'message': 'Event does not exist'
            }, 404

        event_schema = EventSchema()
        result = event_schema.dump(event)

        return {
            'success': 'true',
            'message': 'message retrieved successfully',
            'event': result.data
        }, 200

    def put(self, eventId):
        try:
            event = Event()
            if 'token' not in request.headers:
                return {
                    'message': 'User not signed in'
                }, 401

            token = request.headers['token']
            user_id = event.decode_token(token)
            updateEvent = Event.query.get(eventId)

            if not updateEvent:
                return {
                    'success': 'false',
                    'message': 'Event does not exist'
                }, 404
        
            if user_id != updateEvent.user_id:
                return {
                    'message': 'You do not have permission to edit this event'
                }, 401

            if not request.form['event_name'] or not request.form['event_date']:
                pass

            updateEvent.event_name = request.form['event_name']
            updateEvent.event_date = request.form['event_date']

            db.session.add(updateEvent)
            db.session.commit()

            event_schema = EventSchema()
            result = event_schema.dump(updateEvent)
            return {
                'success': 'true',
                'message': 'event updated successfully',
                'event': result.data
            }, 201

        except KeyError as error:
                raise ValidationError('Invalid entries, missing ' + error.args[0])

    def delete(self, eventId):
        event = Event()
        if 'token' not in request.headers:
            return {
                'message': 'User not signed in'
            }, 401

        token = request.headers['token']
        user_id = event.decode_token(token)
        delete_event = Event.query.get(eventId)

        if not delete_event:
            return jsonify({
                'success': 'false',
                'message': 'Event does not exist'
            }), 404

        if user_id != delete_event.user_id:
            return {
                'message': 'You do not have permission to delete this event'
            }, 401

        db.session.delete(delete_event)
        db.session.commit()

        return {
            'success': 'true',
            'message': 'Event deleted successfully'
        }, 200


event_api.add_resource(Events, '/events')
event_api.add_resource(SingleEvent, '/events/<int:eventId>')
