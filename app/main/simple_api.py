from . import main

@main.route('/', methods=['GET', 'POST'])
def index():
  print 'here is log'
  return 'hello'
