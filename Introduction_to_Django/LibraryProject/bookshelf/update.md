# Update

Command:
```python
from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
book.title = "Nineteen Eighty-Four"
book.save()
book.title
#outcome
'Nineteen Eighty-Four'

#or

from bookshelf.models import Book
b = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.filter(id=b.id).values()
# Expected output:
# [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]