from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from models import UserModel
import datetime

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help="This field cannot be blank.")
parser.add_argument('password', type=str, required=True, help="This field cannot be blank.")

class UserRegister(Resource):
    def post(self):
        data = parser.parse_args()
        if UserModel.query.filter_by(username=data['username']).first():
            return {'message': 'User already exists'}, 400

        user = UserModel(username=data['username'], password=data['password'])
        db.session.add(user)
        db.session.commit()

        return {'message': 'User created successfully'}, 201

class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        user = UserModel.query.filter_by(username=data['username']).first()

        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id, expires_delta=datetime.timedelta(hours=1))
            return {'access_token': access_token}, 200

        return {'message': 'Invalid credentials'}, 401

class UserLogout(Resource):
    @jwt_required()
    def post(self):
        jti = get_jwt()['jti']
        return {'message': 'Successfully logged out'}, 200
