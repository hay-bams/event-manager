import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  ''' parent configuration class '''
  DEBUG = False
  SECRET_KEY = 'our event secret is only known by us'
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/event_manager'
  # FLASK_DEBUG=1

class DevelopmentConfig(Config):
  ''' configuration for development '''
  DEBUG = True

class TestingConfig(Config):
  ''' configuration for test '''
  TESTING = True
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://localhost/event_manager_test'
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
