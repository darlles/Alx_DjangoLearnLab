from rest_framework import generics, permissions, filters
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

# ListView: Retrieve all books
class BookListView(generics.ListAPIView):
    """
    Provides a read-only endpoint to list all books.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # anyone can view


# DetailView: Retrieve a single book by ID
class BookDetailView(generics.RetrieveAPIView):
    """
    Provides a read-only endpoint to retrieve a single book by ID.
    Accessible to both authenticated and unauthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# CreateView: Add a new book
class BookCreateView(generics.CreateAPIView):
    """
    Provides an endpoint to create a new book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """
        Hook to customize creation behavior.
        For example, you could attach the current user as the author.
        """
        serializer.save()


# UpdateView: Modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Provides an endpoint to update an existing book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        """
        Hook to customize update behavior.
        Ensures validation runs before saving.
        """
        serializer.save()


# DeleteView: Remove a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Provides an endpoint to delete a book.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]



     # Enable filtering, searching, ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Filtering fields
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Search fields
    search_fields = ['title', 'author__name']

    # Ordering fields
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
