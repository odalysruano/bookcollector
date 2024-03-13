from django.shortcuts import render
from django.views.generic.edit import CreateView

# Import the Book Model
from .models import Book

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    books = Book.objects.all() # Retrieve all books
    return render(request, 'books/index.html', {
        'books': books
})

def books_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'books/detail.html', { 'book': book })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'
