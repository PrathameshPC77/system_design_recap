from django.shortcuts import render

# Create your views here.
# core/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World! (Secure if HTTPS)</h1>")
