# blog/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
from .models import Post, Tag
from .models import Comment

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'avatar')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 4}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post...'}),
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write a comment...'}),
        }

    def clean_content(self):
        content = self.cleaned_data.get('content', '').strip()
        if not content:
            raise forms.ValidationError("Comment cannot be empty.")
        return content
    
class PostForm(forms.ModelForm):
    # Accept comma-separated tags; optional
    tags_input = forms.CharField(
        required=False,
        help_text="Comma-separated tags (e.g., django, web, tutorial)"
    )

    class Meta:
        model = Post
        fields = ('title', 'content', 'tags_input')
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title'}),
            'content': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write your post...'}),
        }

    def _get_or_create_tags(self, tags_csv):
        names = [t.strip() for t in tags_csv.split(',') if t.strip()]
        tag_objs = []
        for name in names:
            tag, _ = Tag.objects.get_or_create(name__iexact=name, defaults={'name': name})
            tag_objs.append(tag)
        return tag_objs

    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
        tags_csv = self.cleaned_data.get('tags_input', '')
        if tags_csv:
            tags = self._get_or_create_tags(tags_csv)
            post.tags.set(tags)
        else:
            # If not provided, keep existing tags when updating; clear only if explicitly empty string submitted
            if self.instance.pk and 'tags_input' in self.cleaned_data and self.cleaned_data['tags_input'] == '':
                post.tags.clear()
        if commit:
            self.save_m2m()
        return post

    def initial_from_instance(self, instance):
        # Helper for views to prefill tags_input on edit
        return ', '.join(instance.tags.values_list('name', flat=True))
