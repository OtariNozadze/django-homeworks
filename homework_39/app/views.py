from django.shortcuts import render, redirect
from .models import Category, Book
from .forms import BookForm

def index(request):
    filter_book = request.GET.get('search')
    filter_category = request.GET.getlist('category')

    if filter_book:
        books = Book.objects.filter(name__icontains=filter_book)
    elif filter_category:
        books = Book.objects.filter(categories__in=filter_category)
    else:
        books = Book.objects.all()

    categories = Category.objects.all()
    return render(request, 'index.html', {'books': books, 'categories': categories})



def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})