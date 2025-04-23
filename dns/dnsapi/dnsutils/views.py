from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
import socket, time
import dns.resolver

dns_cache = {}

@api_view(["GET"])
def resolve_domain(request, domain):
    try:
        ip = socket.gethostbyname(domain)
        return Response({"domain": domain, "ip": ip})
    except:
        return Response({"error": "DNS resolution failed"}, status=400)

@api_view(["GET"])
def query_record(request, domain, record_type):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        result = [answer.to_text() for answer in answers]
        return Response({record_type: result})
    except Exception as e:
        return Response({"error": str(e)}, status=400)

@api_view(["GET"])
def cached_resolve(request, domain):
    ttl = 300
    if domain in dns_cache:
        cached_time, ip = dns_cache[domain]
        if time.time() - cached_time < ttl:
            return Response({"domain": domain, "ip": ip, "cached": True})
    try:
        ip = socket.gethostbyname(domain)
        dns_cache[domain] = (time.time(), ip)
        return Response({"domain": domain, "ip": ip, "cached": False})
    except:
        return Response({"error": "DNS resolution failed"}, status=400)
