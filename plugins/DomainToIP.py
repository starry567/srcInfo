import socket

def resolve_domain(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        pass

if __name__ == '__main__':
    ip = resolve_domain("www.tibetpolicy.net")
    print(ip)
