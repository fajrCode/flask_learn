from flask import Flask
from app.config.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from app.routes import api, main, dosen, mahasiswa

app.register_blueprint(main.Main)
app.register_blueprint(api.Api, url_prefix="/api")
app.register_blueprint(dosen.Dosen,url_prefix="/dosen")
app.register_blueprint(mahasiswa.Mahasiswa,url_prefix="/mahasiswa")