import os
import jwt
from app import db
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash
from config import app_config
from app.models.model_operations import ModelOperations

token_secret = os.getenv('TOKEN_SECRET')


class User(db.Model, ModelOperations):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), index=True, nullable=False)
    events = db.relationship(
      'Event',
      backref='user',
      lazy='dynamic')

    def set_password_hash(self, password):
        self.password = generate_password_hash(password)

    def verify_password(self, password):
        password_hash = self.password
        return check_password_hash(password_hash, password)

    def encode_token(self):
        """
        Generate the auth token
        :return: string
        """
        try:
            payload = {
              'exp': datetime.utcnow() + timedelta(days=0, seconds=30, minutes=30),
              'iat': datetime.utcnow(), 
              'sub': self.id
            }

            return jwt.encode(payload, token_secret, algorithm='HS256')

        except Exception as error:
            return error

    def __repr__(self):
        return '<User {}>'.format(self.username)

