from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse

def backend_view(request):
    return JsonResponse({"message": "Hello from Backend!"})

