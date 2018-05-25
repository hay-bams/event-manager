from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from app.user import errors

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.error_handler()
def unauthorized():
    return errors.error_response(401, 'please signin')