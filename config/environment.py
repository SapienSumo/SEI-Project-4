import os

db_uri = os.getenv('DATABASE_URL', 'postgres://localhost:5432/book-db')
secret = os.getenv('SECRET', 'placeholder')
