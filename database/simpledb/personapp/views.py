from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Person

def add_person(request):
    Person.objects.create(name="Alice", age=30)
    return JsonResponse({"message": "Person added"})

def list_people(request):
    people = list(Person.objects.values())
    return JsonResponse(people, safe=False)
