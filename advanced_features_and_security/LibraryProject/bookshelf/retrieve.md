# Retrieve

Command:
```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year

outcome
('1984', 'George Orwell', 1949)

#or

from bookshelf.models import Book
books = Book.objects.all()
list(books.values())
# Expected output:
# [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]