# task_marshmallow.py
from marshmallow import Schema, fields

class TaskSchema(Schema):
    id = fields.Int(required=True, example=1)
    title = fields.Str(required=True, example="Fix bugs")
    status = fields.Str(required=True, example="in_progress")