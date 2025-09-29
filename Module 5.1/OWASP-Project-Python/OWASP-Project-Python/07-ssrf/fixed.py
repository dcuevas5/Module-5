# fixed.py - SSRF mitigation (simple allowlist)
import requests, urllib.parse
ALLOWED={'example.com','api.example.com'}
def allowed(url):
    try:
        h=urllib.parse.urlparse(url).hostname
        return h in ALLOWED
    except:
        return False
if __name__=='__main__':
    url=input('Enter URL: ')
    if not allowed(url): print('not allowed'); exit(1)
    print('would fetch',url)
