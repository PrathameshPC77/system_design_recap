import socket
import ipaddress

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def validate_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False

def resolve_dns(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        return "Resolution failed"

def subnet_details(cidr):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
        return {
            "Network": str(network.network_address),
            "Netmask": str(network.netmask),
            "Broadcast": str(network.broadcast_address),
            "Usable Hosts (first 3)": [str(ip) for ip in list(network.hosts())[:3]]
        }
    except ValueError:
        return "Invalid CIDR notation"


# Test Outputs
print("➡️ Local IP:", get_local_ip())
print("➡️ Validate '192.168.1.1':", validate_ip("192.168.1.1"))
print("➡️ Validate '256.1.1.1':", validate_ip("256.1.1.1"))
print("➡️ Google IP:", resolve_dns("google.com"))
print("➡️ Subnet Info:", subnet_details("192.168.1.0/24"))
