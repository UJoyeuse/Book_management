from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Author
from .serializers import BookSerializer
from .serializers import AuthorSerializer
from .models import Book
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def author_list(request):
        authors=Author.objects.all()
        serializer=AuthorSerializer(authors, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def book_list(request):
   
       books=Book.objects.all()
       serializer=BookSerializer(books, many=True)
       return Response(serializer.data)

@api_view(['POST'])
def authorCreate(request):
        serializer=AuthorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)   

@api_view(['POST'])
def bookCreate(request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)   

@api_view(['PUT'])
def authorUpdate(request, pk):
      authors=Author.objects.get(id=pk)
      serializer=AuthorSerializer(instance=authors, data=request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)          

@api_view(['PUT'])
def bookUpdate(request, pk):
      books=Book.objects.get(id=pk)
      serializer=BookSerializer(instance=books, data=request.data)
      if serializer.is_valid():
            serializer.save()
      return Response(serializer.data)                             
          
@api_view(['DELETE'])
def authorDelete(request, pk):
     authors=Author.objects.get(id=pk)
     authors.delete()
     return Response("successfully deleted")  

@api_view(['DELETE'])
def bookDelete(request, pk):
     books=Book.objects.get(id=pk)
     books.delete()
     return Response("successfully deleted")   
        
  
