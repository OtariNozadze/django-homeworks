from django.shortcuts import render, redirect
from .models import Category, Book
from .forms import BookForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
import logging

logger = logging.getLogger(__name__)
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

    paginator = Paginator(books, 6)

    try:
        page_num = request.GET.get('page')
        books = paginator.page(page_num)
        logger.info(f'page: {page_num}')
    except PageNotAnInteger:
        books = paginator.page(1)
        logger.error('Not an Integer')
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
        logger.error(f'Redirecting to {paginator.num_pages}')

    return render(request, 'index.html', {'books': books, 'categories': categories})


@login_required(login_url='/users/login/')
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app:index')
    else:
        form = BookForm()
        return render(request, 'add_book.html', {'form': form})
    
def book_details(request, pk):
    book = Book.objects.get(pk=pk)
    related_books = Book.objects.filter(categories__in=book.categories.all()).exclude(pk=pk)
    return render(request, 'book_details.html', {'book': book, 'related_books': related_books})