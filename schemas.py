from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    password = fields.Str()

class ItemSchema(Schema):
    id = fields.Int()
    name = fields.Str()
    price = fields.Float()
