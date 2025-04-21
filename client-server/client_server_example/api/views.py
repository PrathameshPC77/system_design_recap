from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def user(request):
    data = {
        "message": "Hello from Django Server!",
        'username': 'prathamesh',
        'email': 'prathamesh@example.com',
        'skills': ['Python', 'Django', 'System Design']
    }
    return JsonResponse(data)

