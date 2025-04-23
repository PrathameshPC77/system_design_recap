import socket
import dns.resolver
import time

dns_cache = {} #In-memory DNS Cache

# 1 Resolve DNS using socket
def resolve_dns(domain):
    try:
        ip = socket.gethostbyname(domain)
        return f"{domain} → {ip}"
    except socket.gaierror:
        return "DNS resolution failed"

#2. Query specific DNS records (A, MX, etc.)
def query_dns(domain, record_type="A"):
    try:
        answers = dns.resolver.resolve(domain, record_type)
        return [answer.to_text() for answer in answers]
    except Exception as e:
        return [str(e)]

# 3. DNS resolution with caching (TTL simulation)
def cached_resolve(domain, ttl=300):
    if domain in dns_cache:
        cached_time, ip = dns_cache[domain]
        if time.time() - cached_time < ttl:
            return f"(cached) {domain} → {ip}"
    try:
        ip = socket.gethostbyname(domain)
        dns_cache[domain] = (time.time(), ip)
        return f"(fresh) {domain} → {ip}"
    except socket.gaierror:
        return "DNS resolution failed"

# --- Testing all functionalities ---
if __name__ == "__main__":
    domain = "google.com"

    print("1. DNS Resolve:")
    print(resolve_dns(domain))

    print("\n2. DNS Records:")
    print("A Record:", query_dns(domain, "A"))
    print("MX Record:", query_dns(domain, "MX"))
    print("NS Record:", query_dns(domain, "NS"))

    print("\n3. Cached DNS Resolve:")
    print(cached_resolve(domain))     # fresh
    time.sleep(2)
    print(cached_resolve(domain))     # cached
