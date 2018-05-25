import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import app_config
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
migrate = Migrate()
config_name = os.getenv('FLASK_ENV')
ma = Marshmallow()

def create_app(config_class=app_config['development']):
  app = Flask(__name__)
  app.config.from_object(config_class)
  db.init_app(app)
  migrate.init_app(app, db)
  ma.init_app(app)
  
  from app.center import center_api 
  app.register_blueprint(center_api, url_prefix = '/api')

  from app.user import user_api
  app.register_blueprint(user_api, url_prefix = '/api')

  from app.event import event_api
  app.register_blueprint(event_api, url_prefix = '/api')

  return app

from app import models