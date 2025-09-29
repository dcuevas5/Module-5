# vulnerable.py - SSRF (naive requests.get)
import requests
url = input('Enter URL: ')
r = requests.get(url)
print(r.status_code, r.text[:200])
