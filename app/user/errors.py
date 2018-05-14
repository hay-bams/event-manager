from flask import jsonify
from app.user import user_api
from app.exception import ValidationError
from werkzeug.http import HTTP_STATUS_CODES

def error_response(status_code, message=None):
  payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
  if message:
    payload['message'] = message
    payload['status'] = status_code
  response = jsonify(payload)
  response.status_code = status_code
  return response

@user_api.app_errorhandler(ValidationError)
def bad_request(e):
  return error_response(400, e.args[0])

@user_api.app_errorhandler(404)
def not_found(e):
  return error_response(404, 'Invalid resource URI')
  # response = jsonify({'status': 404, 'error': 'not found',
  #                     'message': 'invalid Resource URI'})
  # response.status_code = 404
  # return response

@user_api.app_errorhandler(500)  # this has to be an app-wide handler
def internal_server_error(e):
  db.session.rollback()
  return error_response(500, e.args[0])
  # response = jsonify({'status': 500, 'error': 'internal server error',
  #                     'message': e.args[0]})
  # response.status_code = 500
  # return response
    