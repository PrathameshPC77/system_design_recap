from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .utils import measure_http_latency, get_cached_data, simulate_slow_task

def latency_view(request):
    latency = measure_http_latency("https://www.google.com")
    return JsonResponse({"google.com_latency": latency})

def cached_view(request):
    result = get_cached_data()
    return JsonResponse({"result": result})

def simulate_view(request):
    simulate_slow_task()
    return JsonResponse({"message": "Slow task started"})
