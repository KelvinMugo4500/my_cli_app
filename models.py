from database import get_db_connection

class Author:
    @staticmethod
    def create(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO authors (name) VALUES (?)", (name,))
            conn.commit()
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all():
        conn = get_db_connection()
        authors = conn.execute("SELECT * FROM authors").fetchall()
        conn.close()
        return authors

    @staticmethod
    def delete(author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (author_id,))
        conn.commit()
        conn.close()
        return cursor.rowcount

class Book:
    @staticmethod
    def create(title, author_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO books (title, author_id) VALUES (?, ?)", (title, author_id))
            conn.commit()
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all():
        conn = get_db_connection()
        books = conn.execute("SELECT books.id, books.title, authors.name AS author_name "
                             "FROM books JOIN authors ON books.author_id = authors.id").fetchall()
        conn.close()
        return books

    @staticmethod
    def delete(book_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))
        conn.commit()
        conn.close()
        return cursor.rowcount

class Publisher:
    @staticmethod
    def create(name):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("INSERT INTO publishers (name) VALUES (?)", (name,))
            conn.commit()
        except sqlite3.IntegrityError:
            return None
        finally:
            conn.close()
        return cursor.lastrowid

    @staticmethod
    def get_all():
        conn = get_db_connection()
        publishers = conn.execute("SELECT * FROM publishers").fetchall()
        conn.close()
        return publishers

    @staticmethod
    def delete(publisher_id):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM publishers WHERE id = ?", (publisher_id,))
        conn.commit()
        conn.close()
        return cursor.rowcount
