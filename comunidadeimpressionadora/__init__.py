import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)



SECRET_KEY = os.urandom(6)
app.config['SECRET_KEY'] = SECRET_KEY
if os.getenv("URL_DO_BANCO_DE_DADOS"):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("URL_DO_BANCO_DE_DADOS")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'alert-info'


from comunidadeimpressionadora import routes




