from django import forms

class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=100, required=False)

    from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']  # adjust based on your actual model fields