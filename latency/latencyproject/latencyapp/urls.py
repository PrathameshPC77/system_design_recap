from django.urls import path
from . import views

urlpatterns = [
    path('latency/', views.latency_view),
    path('cache/', views.cached_view),
    path('simulate/', views.simulate_view),
]
