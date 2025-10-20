from django import forms
from .models import Textbook

class PostBookForm(forms.ModelForm):
    class Meta:
        model = Textbook
        fields = ['title', 'author', 'course_code', 'edition', 'year']

class SearchBookForm(forms.Form):
    course_code = forms.CharField(label='Course Code', max_length=20)
