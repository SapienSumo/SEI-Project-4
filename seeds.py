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
    Memoir = Genre(name='Memoir')
    Novel = Genre(name='Novel')
    Crime_Fiction = Genre(name='Crime Fiction')
    Literary_fiction = Genre(name='Literary fiction')
    Autobiography = Genre(name='Autobiography')
    Mystery_fiction = Genre(name='Mystery fiction')
    Anthology = Genre(name='Anthology')
    Magical_Realism = Genre(name='Magical Realism')
    Gothic_fiction = Genre(name='Gothic fiction')
    Alternate_history = Genre(name='Alternate history')
    History = Genre(name='History')
    Graphic_novel = Genre(name='Graphic novel')
    Hard_science_fiction = Genre(name='Hard science fiction')
    Self_help_book = Genre(name='Self help book')
    Mystery = Genre(name='Mystery')


    Karen_Travis = Author(name='Karen Travis')
    JRR_Tolkien = Author(name='JRR Tolkien')
    Yuval_Noah_Harari = Author(name='Yuval Noah Harari')
    George_Orwell = Author(name='George Orwell')
    Stefan_Zweig = Author(name='Stefan Zweig')
    Charlotte_Brontë = Author(name='Charlotte Brontë')
    Michelle_Obama = Author(name='Michelle Obama')
    Truman_Capote = Author(name='Truman Capote')
    Sally_Rooney = Author(name='Sally Rooney')
    Benjamin_Franklin = Author(name='Benjamin Franklin')
    Louise_Penny = Author(name='Louise Penny')
    Al_Sarrantonio = Author(name='Al Sarrantonio')
    Percy_Makhuba = Author(name='Percy Makhuba')
    Philip_K_Dick = Author(name='Philip K. Dick')
    Peter_Frankopan = Author(name='Peter Frankopan')
    Bungie = Author(name='Bungie')
    Martha_Wells = Author(name='Martha Wells')
    DK = Author(name='DK')
    Robert_Crais = Author(name='Robert Crais')
    James_Clear = Author(name='James Clear')
    Herodotus = Author(name='Herodotus')
    Bram_Stoker = Author(name='Bram Stoker')


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
        name='Thursday War',
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

    Book(
        name='The Thursday War',
        image='./images/Thursday-war.jpg',
        author=Karen_Travis,
        genres=[Sci_fi],
        user=user
    )

    Book(
        name='Charlotte Brontë',
        image='./images/jane_eyre.jpg',
        author=Charlotte_Brontë,
        genres=[Novel],
        user=user
    )

    Book(
        name='Becoming',
        image='./images/Michelle_Obama.jpg',
        author=Michelle_Obama,
        genres=Memoir,
        user=user
    )

    Book(
        name='In Cold Blood',
        image='./images/cold_blood.jpg',
        author=Truman_Capote,
        genres=Crime_Fiction,
        user=user
    )

    Book(
        name='Normal People',
        image='./images/normal_people.jpg',
        author=Sally_Rooney,
        genres=Literary_fiction,
        user=user
    )

    Book(
        name='Benjamin Franklin',
        image='./images/ben.jpg',
        author=Benjamin_Franklin,
        genres=Autobiography,
        user=user
    )

    Book(
        name='Kingdom of the Blind',
        image='./images/blind.jpg',
        author=Louise_Penny,
        genres=Mystery,
        user=user
    )

    Book(
        name='999',
        image='./images/999.jpg',
        author=Al_Sarrantonio,
        genres=Anthology,
        user=user
    )

    Book(
        name='Cries of the Forgotten',
        image='./images/cries.jpg',
        author=Percy_Makhuba,
        genres=Magical_Realism,
        user=user
    )

    Book(
        name='Dracula',
        image='./images/dracula.jpg',
        author=Bram_Stoker,
        genres=Gothic_fiction,
        user=user
    )

    Book(
        name='The Man in the High Castle',
        image='./images/high-castle.jpg',
        author=Philip_K_Dick,
        genres=Alternate_history,
        user=user
    )

    Book(
        name='The Silk Roads',
        image='./images/slik.jpg',
        author=Peter_Frankopan,
        genres=History,
        user=user
    )

    Book(
        name='The Halo Graphic Novel',
        image='./images/halo-graphic.jpg',
        author=Bungie,
        genres=Graphic_novel,
        user=user
    )

    Book(
        name='All Systems Red',
        image='./images/all-systems-red.jpg',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Artificial Condition',
        image='./images/ai-condition.jpg',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Rouge Protocol',
        image='./images/rouge-p.jpg',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Exit Strategy',
        image='./images/Exit-Strategy.jpg',
        author=Martha_Wells,
        genres=Hard_science_fiction,
        user=user
    )

    Book(
        name='Dinosaurs',
        image='./images/dinos.jpg',
        author=DK,
        genres=Non_Fiction,
        user=user
    )

    Book(
        name='Atomic Habits',
        image='./images/atomic.jpg',
        author=James_Clear,
        genres=Self_help_book,
        user=user
    )

    Book(
        name='The two minute rule',
        image='./images/two-min.jpg',
        author=Robert_Crais,
        genres=Fiction,
        user=user
    )

    Book(
        name='Histories',
        image='./images/histories.jpg',
        author=Herodotus,
        genres=History,
        user=user
    )

    db.commit()
