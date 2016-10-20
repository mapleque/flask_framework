from flask import Blueprint

main = Blueprint('main', __name__)
from . import simple_api, db_api, config_api
