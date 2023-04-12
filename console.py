import pdb
from models.book import Book
from models.author import Author

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("James", "Patterson")
author_repository.save(author1)

author2 = Author("Roald", "Dahl")
author_repository.save(author2)

author3 = Author("Jacqueline", "Wilson")
author_repository.save(author2)

book_1 = Book("Along Came a Spider", author1, 1993)
book_repository.save(book_1)

book_2 = Book("Matilda", author2, 1988)
book_repository.save(book_2)

book_3 = Book("The Illustrated Mum", author3, 1999)
book_repository.save(book_3)

book_4 = Book("Vicky Angel", author2, 2000)
book_repository.save(book_4)


pdb.set_trace()
