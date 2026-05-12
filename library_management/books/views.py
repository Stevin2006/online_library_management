from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from django.contrib.auth.decorators import login_required

@login_required()
def index(request):
    books = Book.objects.all()
    return render(request, 'books/list.html', {'books': books})

@login_required()
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_home')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})

@login_required()
def update_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    form = BookForm(instance=book)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_home')

    return render(request, 'books/add_book.html', {'form': form})

@login_required()
def delete_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    book.delete()
    return redirect('book_home')

