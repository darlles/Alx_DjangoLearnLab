from bookshelf.models import Book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()
list(Book.objects.all().values())
# Expected output:
# []