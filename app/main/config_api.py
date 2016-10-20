from . import main

@main.route('/config', methods=['GET', 'POST'])
def config_api():
  return 'config'
