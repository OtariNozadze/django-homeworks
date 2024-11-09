from django.shortcuts import render
from .models import Category, Book

def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books})



