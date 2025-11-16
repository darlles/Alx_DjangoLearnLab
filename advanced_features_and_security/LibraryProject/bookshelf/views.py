
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article
from .forms import ExampleForm

@permission_required('your_app.can_view', raise_exception=True)
def view_article(request):
    articles = Article.objects.all()
    return render(request, 'view_article.html', {'articles': articles})

@permission_required('your_app.can_create', raise_exception=True)
def create_article(request):
    # logic to create article
    pass

@permission_required('your_app.can_edit', raise_exception=True)
def edit_article(request, article_id):
    # logic to edit article
    pass

@permission_required('your_app.can_delete', raise_exception=True)
def delete_article(request, article_id):
    # logic to delete article
    pass

from django.shortcuts import render
from .models import Book

def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

from django.shortcuts import render
from .models import Book
from .forms import BookSearchForm

def search_books(request):
    form = BookSearchForm(request.GET or None)
    books = Book.objects.none()
    if form.is_valid():
        title = form.cleaned_data['title']
        books = Book.objects.filter(title__icontains=title)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})