from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields, post_load

class Genre(db.Entity):
    name = Required(str)


class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
