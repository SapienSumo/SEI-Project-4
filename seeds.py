from pony.orm import db_session
from app import db
from models.Book import Book
from models.Genre import Genre
from models.User import User, UserSchema
from models.Author import Author

db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():

    Sci_fi = Genre(name='Sci fi')
    Fantasy = Genre(name='Fantasy')
    Non_Fiction = Genre(name='Non Fiction')
    Fiction = Genre(name='Fiction')

    Karen_Travis = Author(name='Karen Travis')
    JRR_Tolkien = Author(name='JRR Tolkien')
    Yuval_Noah_Harari = Author(name='Yuval Noah Harari')
    George_Orwell = Author(name='George Orwell')
    Stefan_Zweig = Author(name='Stefan Zweig')

    schema = UserSchema()
    user = User(
    username='User',
    email='user@user.com',
    password_hash=schema.generate_hash('pass')
    )

    Book(
        name='Mortal Dictata',
        image='./images/mortal-dictata.jpg',
        author=Karen_Travis,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='The Thursday War',
        image='./images/Thursday-war.jpg',
        author=Karen_Travis,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='Sapiens',
        image='./images/sapiens.jpg',
        author=Yuval_Noah_Harari,
        genres=[Non_Fiction],
        user=user
    )

    Book(
        name='Homo Deus',
        image='./images/homo-deus.jpg',
        author=Yuval_Noah_Harari,
        genres=[Non_Fiction],
        user=user
    )

    Book(
        name='1984',
        image='./images/1984.jpg',
        author=George_Orwell,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='21 Lessons for the 21st Century',
        image='./images/21-lessons.jpg',
        author=Yuval_Noah_Harari,
        genres=[Non_Fiction],
        user=user
    )

    Book(
        name='Fantastic Night',
        image='./images/fantastic.jpg',
        author=Stefan_Zweig,
        genres=[Fiction],
        user=user
    )

    db.commit()
