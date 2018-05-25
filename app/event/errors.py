from flask import jsonify
from app.event import event_bp
from app.exception import AuthenticationError, ValidationError
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
  payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
  if message:
    payload['message'] = message
    payload['status'] = status_code
  response = jsonify(payload)
  response.status_code = status_code
  return response

@event_bp.app_errorhandler(ValidationError)
def bad_request(e):
  return error_response(400, e.args[0])

@event_bp.app_errorhandler(AuthenticationError)
def bad_request(e):
  return error_response(400, e.args[0])

@event_bp.app_errorhandler(404)
def not_found(e):
  return error_response(404, 'Invalid resource URI')

@event_bp.app_errorhandler(500)  # this has to be an app-wide handler
def internal_server_error(e):
  db.session.rollback()
  return error_response(500, e.args[0])

  