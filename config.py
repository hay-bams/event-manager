import os
from dotenv import load_dotenv
from pathlib import Path

basedir = os.path.abspath(os.path.dirname(__file__))
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

class Config:
  ''' parent configuration class '''
  DEBUG = False
  SECRET_KEY = 'our event secret is only known by us'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/event_manager'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  # FLASK_DEBUG=1

class DevelopmentConfig(Config):
  ''' configuration for development '''
  DEBUG = True

class TestingConfig(Config):
  ''' configuration for test '''
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://localhost/event_manager_test'
  DEBUG = True

class ProductionConfig(Config):
  ''' configuration for production '''
  DEBUG = False
  TESTING = False

app_config = {
  'development': DevelopmentConfig,
  'testing': TestingConfig,
  'production': ProductionConfig
}
