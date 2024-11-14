from django.shortcuts import render, get_object_or_404
from .models import Book

def index(request):
    books = Book.objects.all()
    return render(request, "book/book_shelf.html", {"books": books})


def book(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, "book/book.html", {"book": book})