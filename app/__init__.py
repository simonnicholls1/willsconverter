from flask import Flask
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


from app import routes
app.config['SECRET_KEY'] = 'you-will-never-guess'

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)