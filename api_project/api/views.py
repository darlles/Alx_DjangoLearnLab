from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing Book instances.
    Provides CRUD operations: list, create, retrieve, update, destroy.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
