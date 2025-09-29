# fixed.py - SRI and CSP example (strings)
html='''<html><head><meta http-equiv="Content-Security-Policy" content="default-src 'self' https://cdn.example.com"></head>
<body><script src="https://cdn.example.com/lib.js" integrity="sha384-..."></script></body></html>'''
if __name__=='__main__': print(html)
