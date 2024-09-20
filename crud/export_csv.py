import csv
import os
from crud.operations import connect_db


def export_csv():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    books = cursor.fetchall()
    conn.close()

    path = os.path.join('exports', 'books.csv')

    with open(path, 'w', newline='') as archive:
        writer = csv.writer(archive)
        writer.writerow(['id', 'title', 'author', 'publication year', 'price'])
        writer.writerows(books)

def import_csv(path):
    with open(path, 'r') as archive:
        reader = csv.reader(archive)
        next(reader)
        conn = connect_db()
        cursor = conn.cursor()
        for row in reader:
            cursor.execute('''
                INSERT INTO livros (titulo, autor, ano_publicacao, preco)
                VALUES (?, ?, ?, ?)
            ''', (row[1], row[2], int(row[3]), float(row[4])))
        conn.commit()
        conn.close()

