from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, Namespace, fields
from models import db
from flask_migrate import Migrate

api = Api()


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

api.init_app(app)
db.init_app(app)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
