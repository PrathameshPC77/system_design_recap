from django.urls import path
from . import views

urlpatterns = [
    path('get-ip/', views.get_ip),
    path('validate-ip/', views.validate_ip_view),
    path('resolve-domain/', views.resolve_domain),
    path('subnet-info/', views.subnet_info),
]
