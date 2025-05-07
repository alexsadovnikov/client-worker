from marshmallow import Schema, fields

class LoginSchema(Schema):
    username = fields.String(required=True, metadata={"example": "admin"})
    password = fields.String(required=True, metadata={"example": "admin"})

class TokenSchema(Schema):
    access_token = fields.String(required=True, metadata={"example": "ey..."})

class UserInfoSchema(Schema):
    user = fields.String(required=True, metadata={"example": "admin"})