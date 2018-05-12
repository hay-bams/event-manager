from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config


db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
  app = Flask(__name__)
  db.init_app(app)
  app.config.from_object(Config)
  migrate.init_app(app, db)
  
  from app.center import center_api 
  app.register_blueprint(center_api)

  from app.user import user_api
  app.register_blueprint(user_api)

  return app

from app import models