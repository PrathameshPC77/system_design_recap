from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_person),
    path('list/', views.list_people),
]
