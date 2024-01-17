from flask import Flask
from app.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
# from app.config.dbConfig import db

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
jwt = JWTManager(app)

from app.routes import Api

app.register_blueprint(Api.api, url_prefix="/api")
app.register_blueprint(Api.dosen)
# app.register_blueprint(Api.mahasiswa, url_prefix="/mahasiswa")

# from app.model import user, dosen, mahasiswa
# from app import route
