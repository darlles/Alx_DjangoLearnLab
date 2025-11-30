from django.contrib.auth.models import User
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD, filtering, searching, ordering, and permissions.
    """

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.client = APIClient()

        # Create author and books
        self.author = Author.objects.create(name="George Orwell")
        self.book1 = Book.objects.create(title="1984", publication_year=1949, author=self.author)
        self.book2 = Book.objects.create(title="Animal Farm", publication_year=1945, author=self.author)

    # ---------- CRUD Tests ----------
    def test_list_books(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_retrieve_book(self):
        response = self.client.get(f"/api/books/{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "1984")

    def test_create_book_requires_authentication(self):
        data = {"title": "Homage to Catalonia", "publication_year": 1938, "author": self.author.id}
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # unauthenticated

        # Authenticate and retry
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/api/books/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        self.client.login(username="testuser", password="password123")
        data = {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(f"/api/books/{self.book1.id}/update/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.delete(f"/api/books/{self.book2.id}/delete/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------- Filtering, Searching, Ordering ----------
    def test_filter_books_by_publication_year(self):
        response = self.client.get("/api/books/?publication_year=1949")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books_by_title(self):
        response = self.client.get("/api/books/?search=Farm")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get("/api/books/?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))