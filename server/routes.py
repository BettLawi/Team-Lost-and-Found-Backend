from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Namespace, Resource, fields
from models import User, db
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db.init_app(app)

# Initialize Flask-Migrate
migrate = Migrate(app, db)

# Initialize Flask-RESTx
api = Api()
api.init_app(app)

# Define API namespace
ns = Namespace('snapstore')
api.add_namespace(ns)

# Define API models
users_schema = api.model('users',{
    "username": fields.String,
    "email": fields.String,
    "role": fields.String
})

# Define API routes
@ns.route('/users')
class Users(Resource):
    @ns.marshal_list_with(users_schema)
    def get(self):
        users = User.query.all()
        return users, 200

# Main entry point
if __name__ == '__main__':
    app.run(port=5555, debug=True)
