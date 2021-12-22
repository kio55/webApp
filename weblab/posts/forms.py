from .models import Post
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'subtitle', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Title',
            }),
            "subtitle": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subtitle',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'example 2021-12-22 14:53:60',
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Text',
            }),
        }