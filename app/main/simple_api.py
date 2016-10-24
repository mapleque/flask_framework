from flask import current_app
from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
  current_app.logger.error('here is log')
  return 'hello'
