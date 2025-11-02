
---

### Single-file submission: CRUD_operations.md
Include the four command blocks and expected outputs in order (Create, Retrieve, Update, Delete). Example structure:

```markdown
# CRUD operations for Book model

## Create
<create command block and expected output>
from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
# Expected output (repr may vary, Django shows the instance):
# <Book: 1984 by George Orwell (1949)>

## Retrieve
<retrieve command block and expected output>
# Retrieve

Command:
```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
b.title, b.author, b.publication_year
#outcome 
('1984', 'George Orwell', 1949)
from bookshelf.models import Book
books = Book.objects.all()
list(books.values())
# Expected output:
# [{'id': 1, 'title': '1984', 'author': 'George Orwell', 'publication_year': 1949}]

## Update
# Update

Command:
from bookshelf.models import Book
book = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
book.title = "Nineteen Eighty-Four"
book.save()
book.title

<update command block and expected output>
from bookshelf.models import Book
b = Book.objects.get(title="1984", author="George Orwell", publication_year=1949)
b.title = "Nineteen Eighty-Four"
b.save()
Book.objects.filter(id=b.id).values()
# Expected output:
# [{'id': 1, 'title': 'Nineteen Eighty-Four', 'author': 'George Orwell', 'publication_year': 1949}]

## Delete
<delete command block and expected output>
from bookshelf.models import Book
b = Book.objects.get(title="Nineteen Eighty-Four")
b.delete()
list(Book.objects.all().values())
# Expected output:
# []