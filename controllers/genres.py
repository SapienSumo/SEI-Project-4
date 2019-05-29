from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Genre import Genre, GenreSchema

router = Blueprint(__name__, 'genres')

@router.route('/genres', methods=['GET'])
@db_session

def index():
    schema = GenreSchema(many=True)
    genres = Genre.select()
    return schema.dumps(genres)


@router.route('/genres', methods=['POST'])
@db_session
def create():

    schema = GenreSchema()

    try:
        data = schema.load(request.get_json())
        genre = Genre(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(genre), 201


@router.route('/categories/<int:genre_id>', methods=['GET'])
@db_session
def show(genre_id):
    schema = GenreSchema()
    genre = Genre.get(id=genre_id)

    if not genre:
        abort(404)

    return schema.dumps(genre)


@router.route('/categories/<int:genre_id>', methods=['PUT'])
@db_session
def update(genre_id):
    schema = GenreSchema()
    genre = Genre.get(id=genre_id)

    if not genre:
        abort(404)

    try:
        data = schema.load(request.get_json())
        genre.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(genre)


@router.route('/categories/<int:category_id>', methods=['DELETE'])
@db_session
def delete(category_id):
    category = Genre.get(id=category_id)

    if not category:
        abort(404)

    category.delete()
    db.commit()

    return '', 204
