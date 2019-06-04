from flask import Flask
from os import os


app = Flask(__name__)


from app import routes
app.config['SECRET_KEY'] = 'you-will-never-guess'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)