from rest_framework import serializers
from . models import Author
from . models import Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields=['id','name','created_at','updated_at']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=['id','created_at','publication_date','publisher','title','updated_at','author']       