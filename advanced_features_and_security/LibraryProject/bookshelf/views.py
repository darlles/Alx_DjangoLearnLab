
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render
from .models import Article

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