# fixed.py - add security headers
from flask import Flask
app=Flask(__name__)
@app.after_request
def headers(r):
    r.headers['X-Frame-Options']='DENY'
    r.headers['X-Content-Type-Options']='nosniff'
    r.headers['Content-Security-Policy']="default-src 'self'"
    return r
@app.route('/')
def index(): return '<h1>with headers</h1>'
if __name__=='__main__': app.run(debug=True)
