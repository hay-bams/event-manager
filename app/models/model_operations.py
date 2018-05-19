import jwt
import os
from app.exception import AuthenticationError, ValidationError

token_secret = os.getenv('TOKEN_SECRET')

class ModelOperations(object):
   def import_data(self, data):
     print(data)
     try:
       for key, value in data.items():
         setattr(self, key, value)
     except KeyError as e:
       raise ValidationError('Invalid entries, missing ' + e.args[0])
     return self
   
   def decode_token(self, auth_token):
     """
     Decodes the auth token
     :param auth_token:
     :return: integer|string
     """
     try:
       payload = jwt.decode(auth_token, token_secret)
       return payload['sub']
     except jwt.ExpiredSignatureError:
       raise AuthenticationError('Token Expired')
     except jwt.InvalidTokenError:
       raise AuthenticationError('Invalid Token')