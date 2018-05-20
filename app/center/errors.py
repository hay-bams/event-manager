# from flask import jsonify
# from app.center import center_api
# from app.exception import ValidationError

# @center_api.app_errorhandler(ValidationError)
# def bad_request(e):
#   response = jsonify({'status': 400, 'error': 'bad request', 
#                       'message': e.args[0]})
#   response.status_code = 400
#   return response

# @center_api.app_errorhandler(404)
# def not_found(e):
#   response = jsonify({'status': 404, 'error': 'not found',
#                       'message': 'invalid Resource URI'})
#   response.status_code = 404
#   return response

# @center_api.app_errorhandler(500)
# def internal_server_error(e):
#   response = jsonify({'status': 500, 'error': 'internal server error',
#                       'message': e.args[0]})
#   response.status_code = 500
#   return response