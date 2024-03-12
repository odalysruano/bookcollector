from django.shortcuts import render

books = [
    {'name': 'Tomorrow, Tomorrow, and Tomorrow', 'author': 'Gabrielle Zevin' , 'description': 'The novel follows the relationship between three friends who begin a successful video game company together.'},
    {'name': 'Beautiful World, Where Are You', 'author': 'Sally Rooney', 'description': '"Beautiful world, where are you?" is a question two main female characters, best friends from college now on the cusp of 30, grapple with repeatedly in their struggles to figure out how they should live and find meaning in a troubled world that has become increasingly unviable on multiple levels — ecologically, economically, ethically and emotionally.' }
]

# Create your views here.

# Define the home view
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def books_index(request):
    return render(request, 'books/index.html', {
        'books': books
})
