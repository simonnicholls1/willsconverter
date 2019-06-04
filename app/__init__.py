from flask import Flask
from os import os


app = Flask(__name__)


from app import routes
app.config['SECRET_KEY'] = 'you-will-never-guess'

if __name__ == '__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port, debug=True)