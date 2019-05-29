import os

secret = os.getenv('SECRET', 'placeholder')
db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/book-db')
