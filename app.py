from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from db import db
from resources.item import ItemResource
from resources.user import UserRegister, UserLogin, UserLogout

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

api = Api(app)
jwt = JWTManager(app)

db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(ItemResource, '/item/<string:name>')
api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')

if __name__ == '__main__':
    app.run(debug=True)
