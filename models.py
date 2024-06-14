# models.py
from database import get_db_connection

class Author:
    @classmethod
    def create(cls, name):
        conn = get_db_connection()
        conn.execute('INSERT INTO authors (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, author_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM authors WHERE id = ?', (author_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM authors')
        authors = cursor.fetchall()
        conn.close()
        return authors

    @classmethod
    def find_by_id(cls, author_id):
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM authors WHERE id = ?', (author_id,))
        author = cursor.fetchone()
        conn.close()
        return author

class Book:
    @classmethod
    def create(cls, title, author_id):
        conn = get_db_connection()
        conn.execute('INSERT INTO books (title, author_id) VALUES (?, ?)', (title, author_id))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, book_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM books WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM books')
        books = cursor.fetchall()
        conn.close()
        return books

    @classmethod
    def find_by_id(cls, book_id):
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM books WHERE id = ?', (book_id,))
        book = cursor.fetchone()
        conn.close()
        return book

class Publisher:
    @classmethod
    def create(cls, name):
        conn = get_db_connection()
        conn.execute('INSERT INTO publishers (name) VALUES (?)', (name,))
        conn.commit()
        conn.close()

    @classmethod
    def delete(cls, publisher_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM publishers WHERE id = ?', (publisher_id,))
        conn.commit()
        conn.close()

    @classmethod
    def get_all(cls):
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM publishers')
        publishers = cursor.fetchall()
        conn.close()
        return publishers

    @classmethod
    def find_by_id(cls, publisher_id):
        conn = get_db_connection()
        cursor = conn.execute('SELECT * FROM publishers WHERE id = ?', (publisher_id,))
        publisher = cursor.fetchone()
        conn.close()
        return publisher
