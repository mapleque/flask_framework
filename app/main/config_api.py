import json
from . import main
from flask import current_app

@main.route('/config', methods=['GET', 'POST'])
def config_api():
  return json.dumps(current_app.config['SAMPLE'])
