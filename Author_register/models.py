from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField()
    updated_at=models.DateTimeField()

class Book(models.Model):
    created_at = models.DateField()
    publication_date = models.DateField()
    publisher = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    updated_at = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)    
