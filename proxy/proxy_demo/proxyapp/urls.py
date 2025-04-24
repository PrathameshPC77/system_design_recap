from django.urls import path
from .views import backend_view

urlpatterns = [
    path('hello/', backend_view),
]
