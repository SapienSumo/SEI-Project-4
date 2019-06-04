from app import db
from pony.orm import Required, Set
from marshmallow import Schema, fields, post_load

class Genre(db.Entity):
    name = Required(str)
    books = Set('Book')

class GenreSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    books = fields.Nested('BookSchema', many=True, exclude=('genre',), dump_only=True)
    book_ids = fields.List(fields.Int(), load_only=True)

    @post_load
    def load_genres(self, data):
        data['books'] = [Genre.get(id=genre_id) for genre_id in data['Book_ids']]
        del data['Book_ids']

        return data
