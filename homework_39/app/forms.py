from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'categories': forms.CheckboxSelectMultiple(attrs={'class': 'form-control d-flex'})
        }