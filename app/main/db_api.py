import json
from . import main
from .. import db

@main.route('/db', methods=['GET', 'POST'])
def db_api():
  ret = db.session.execute('show tables').fetchall()
  return json.dumps(ret[0][0])
