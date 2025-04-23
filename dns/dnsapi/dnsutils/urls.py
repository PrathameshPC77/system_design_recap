from django.urls import path
from . import views

urlpatterns = [
    path("resolve/<str:domain>/", views.resolve_domain),
    path("dns-query/<str:domain>/<str:record_type>/", views.query_record),
    path("cached-resolve/<str:domain>/", views.cached_resolve),
]
