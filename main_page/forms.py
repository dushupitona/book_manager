from django import forms
from main_page.models import BookModel

class BookForm(forms.ModelForm):
    class Meta:
        model = BookModel
        fields = ['book_name', 'book_author', 'book_img']