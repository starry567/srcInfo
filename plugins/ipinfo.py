import requests
import json

def IP_info(scan_ip):
    url = f"http://ipinfo.io/{scan_ip}/json"
    try:
        r = requests.get(url, timeout=5)
        data = r.json()
        return data
    except requests.exceptions.RequestException as e:
        pass

if __name__ == '__main__':
    IP_infomation = IP_info("139.159.140.130")

