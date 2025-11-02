from bookshelf.models import Book
b = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
b
# Expected output (repr may vary, Django shows the instance):
# <Book: 1984 by George Orwell (1949)>
