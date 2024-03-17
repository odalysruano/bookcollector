from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Import models
from .models import Book, Genre
from .forms import ReviewForm

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
    id_list = book.genres.all().values_list('id')
    genres_book_doesnt_have = Genre.objects.exclude(id_in=id_list)
    review_form = ReviewForm()
    return render(request, 'books/detail.html', { 'book': book, 'review_form': review_form, 'genre': genres_book_doesnt_have })

def add_review(request, book_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.book_id = book_id
        new_review.save()
    return redirect('detail', book_id=book_id)        

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'description', 'year_published']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'        
