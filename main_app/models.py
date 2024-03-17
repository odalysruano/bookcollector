from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Genre(models.Model):
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year_published = models.IntegerField()

    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'book_id': self.id})

class Review(models.Model):
    date = models.DateField('Date Finished')
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    review = models.CharField(max_length=250)

    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f" A {self.rating} star rating on {self.date}!"
    
    class Meta:
        ordering = ['-date']
    