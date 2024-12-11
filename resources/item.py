from flask_restful import Resource
from flask_jwt_extended import jwt_required
from models import ItemModel

class ItemResource(Resource):
    @jwt_required()
    def get(self, name):
        item = ItemModel.query.filter_by(name=name).first()
        if item:
            return {'name': item.name, 'price': item.price}, 200
        return {'message': 'Item not found'}, 404
