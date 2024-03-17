from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

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
    genres_book_doesnt_have = Genre.objects.exclude(id__in=id_list)
    review_form = ReviewForm()
    return render(request, 'books/detail.html', { 'book': book, 'review_form': review_form, 'genres': genres_book_doesnt_have })

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['author', 'description', 'year_published']

class BookDelete(DeleteView):
    model = Book
    success_url = '/books'

def add_review(request, book_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.book_id = book_id
        new_review.save()
    return redirect('detail', book_id=book_id)  

class GenreList(ListView):
    model = Genre

class GenreDetail(DetailView):
    model = Genre

class GenreCreate(CreateView):
    model = Genre
    fields = '__all__'

class GenreUpdate(UpdateView):
    model = Genre
    fields = '__all__'

class GenreDelete(DeleteView):
    model = Genre
    success_url = '/genres'

def assoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.add(genre_id)
    return redirect('detail', book_id=book_id)

def unassoc_genre(request, book_id, genre_id):
    Book.objects.get(id=book_id).genres.remove(genre_id)
    return redirect('detail', book_id=book_id)
