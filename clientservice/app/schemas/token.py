# clientservice/auth/app/schemas/token.py

from marshmallow import Schema, fields

class LoginRequest(Schema):
    username = fields.Str(required=True, example="admin")
    password = fields.Str(required=True, example="admin")

class TokenResponse(Schema):
    access_token = fields.Str(required=True, example="JWT токен")

class UserInfoResponse(Schema):
    user = fields.Str(required=True, example="admin")