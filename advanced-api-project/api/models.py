from django.db import models

class Author(models.Model):
    """
    Represents an author entity.
    Each author can have multiple books associated with them.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book entity.
    Each book is linked to a single author (one-to-many relationship).
    """
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"