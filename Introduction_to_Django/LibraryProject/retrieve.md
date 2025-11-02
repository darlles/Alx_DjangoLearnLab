from bookshelf.models import Book
books = Book.objects.all()
list(books.values())
# Expected output:
# [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]