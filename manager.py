from flask import Flask
from app import create_app

app = create_app('../config/default.py')

if __name__ == '__main__':
  app.run()
