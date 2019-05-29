from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields

class Author(db.Entity):
    name = Required(str)
    books = Set('Book')

class AuthorSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    books = fields.Nested('BookSchema', many=True, exclude=('genres',))
