import os.path
import sqlite3


def connect_db():
    db_dir = os.path.join('data', 'library.db')

    return sqlite3.connect(db_dir)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            autor TEXT NOT NULL,
            ano_publicacao INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def add_book(title: str, author: str, year, price: float):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO livros (titulo, autor, ano_publicacao, preco)
        VALUES (?, ?, ?, ?)
    ''', (title, author, year, price))
    conn.commit()
    conn.close()

def show_books():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    books = cursor.fetchall()
    conn.close()
    for i in books:
        print(i)

def search_book_by_author(author):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros WHERE autor = ?', (author,))
    books = cursor.fetchall()
    conn.close()
    for i in books:
        print(i)

def update_price(book_id: int, new_price: float):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE livros
        SET preco = ?
        WHERE id = ?
    ''', (new_price, book_id))
    conn.commit()
    conn.close()

def remove_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM livros WHERE id = ?', (book_id,))
    conn.commit()
    conn.close()