from db.run_sql import run_sql

from models.book import Book
from models.author import Author
import repositories.author_repository as author_repository


def save(book):
    sql = "INSERT INTO books (title, author_id, genre, year_of_release) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author.id, book.genre, book.year_of_release]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        author = author_repository.select(row['author_id'])
        book = Book(row['title'], author, row['genre'], row['year_of_release'], row['id'] )
        books.append(book)
    return books



def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        author = author_repository.select(result['author_id'])
        book = Book(result['title'], author, result['genre'], result['year_of_release'], result['id'] )
    return book


def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(book):
    sql = "UPDATE books SET (title, author_id, genre, year_of_release) = (%s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author.id, book.genre, book.year_of_release]
    run_sql(sql, values)
