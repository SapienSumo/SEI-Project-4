from flask import Blueprint, request, jsonify, abort
from pony.orm import db_session
from marshmallow import ValidationError
from app import db
from models.Author import Author, AuthorSchema

router = Blueprint(__name__, 'authors')

@router.route('/authors', methods=['GET'])
@db_session

def index():
    schema = AuthorSchema(many=True)
    authors = Author.select()
    return schema.dumps(authors)

@router.route('/authors', methods=['POST'])
@db_session
def create():
    schema = AuthorSchema()

    try:
        data = schema.load(request.get_json())
        author = Author(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(author), 201


@router.route('/authors/<int:author_id>', methods=['GET'])
@db_session
def show(author_id):
    schema = AuthorSchema()
    author = Author.get(id=author_id)

    if not author:
        abort(404)

    return schema.dumps(author)


@router.route('/authors/<int:author_id>', methods=['PUT'])
@db_session
def update(author_id):
    schema = AuthorSchema()
    author = Author.get(id=author_id)

    if not author:
        abort(404)

    try:
        data = schema.load(request.get_json())
        author.set(**data)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return schema.dumps(author)


@router.route('/authors/<int:author_id>', methods=['DELETE'])
@db_session
def delete(author_id):
    author = Author.get(id=author_id)

    if not author:
        abort(404)

    author.delete()
    db.commit()

    return '', 204
