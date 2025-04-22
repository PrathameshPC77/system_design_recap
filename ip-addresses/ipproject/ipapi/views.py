from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import get_local_ip, validate_ip, resolve_dns, subnet_details

@api_view(['GET'])
def get_ip(request):
    return Response({"local_ip": get_local_ip()})

@api_view(['GET'])
def validate_ip_view(request):
    ip = request.GET.get('ip')
    if ip is None:
        return Response({"error": "Missing 'ip' parameter"})
    return Response({"ip": ip, "is_valid": validate_ip(ip)})

@api_view(['GET'])
def resolve_domain(request):
    domain = request.GET.get('domain')
    if domain is None:
        return Response({"error": "Missing 'domain' parameter"})
    result = resolve_dns(domain)
    return Response({"domain": domain, "resolved_ip": result if result else "Resolution failed"})

@api_view(['GET'])
def subnet_info(request):
    cidr = request.GET.get('cidr')
    if cidr is None:
        return Response({"error": "Missing 'cidr' parameter"})
    result = subnet_details(cidr)
    return Response({"cidr": cidr, "details": result if result else "Invalid CIDR"})
