from django.urls import path
from .views import hello_api, BookListCreate

urlpatterns = [
    path('api/hello/', hello_api),
    path('api/books/', BookListCreate.as_view()),
]

