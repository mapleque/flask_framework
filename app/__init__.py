from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from logging.handlers import RotatingFileHandler

db = SQLAlchemy()

def create_app(config_name):
  app = Flask(__name__)
  app.config.from_pyfile(config_name)
  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)
  handler = RotatingFileHandler('/tmp/flask.log')
  app.logger.addHandler(handler)
  db.init_app(app)

  return app
