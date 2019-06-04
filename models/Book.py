from app import db
from pony.orm import Required, Optional, Set
from marshmallow import Schema, fields, post_load

from .User import User
from .Author import Author
from .Genre import Genre

class Book(db.Entity):
    name = Required(str)
    author = Required('Author')
    genres = Set('Genre')
    user = Required('User')
    image = Required(str)
    blurb = Required(str)

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    image = fields.Str(required=False)
    blurb = fields.Str(required=False)
    author = fields.Nested('AuthorSchema', exclude=('books',), dump_only=True)
    author_id = fields.Int(load_only=True)
    genres = fields.Nested('GenreSchema', many=True, exclude=('books',), dump_only=True)
    genre_ids = fields.List(fields.Int(), load_only=True)
    user = fields.Nested('UserSchema', )

    @post_load
    def load_author(self, data):
        data['author'] = Author.get(id=data['author_id'])
        del data['author_id']

        return data

    @post_load
    def load_genres(self, data):
        data['genres'] = [Genre.get(id=genre_id) for genre_id in data['genre_ids']]
        del data['genre_ids']

        return data
