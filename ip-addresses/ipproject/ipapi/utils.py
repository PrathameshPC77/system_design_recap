import socket
import ipaddress

def get_local_ip():
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

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
        return None

def subnet_details(cidr):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
        return {
            "Network": str(network.network_address),
            "Netmask": str(network.netmask),
            "Broadcast": str(network.broadcast_address),
            "UsableHosts": [str(ip) for ip in list(network.hosts())[:3]]
        }
    except ValueError:
        return None
