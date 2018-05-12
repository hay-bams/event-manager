import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY = 'our event secret is only known by us'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/event_manager'
  FLASK_DEBUG=1