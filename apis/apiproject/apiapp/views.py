from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

@api_view(['GET'])
def hello_api(request):
    return Response({"message": "Hello API!"})

class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
