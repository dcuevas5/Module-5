# fixed.py - token-based reset (demo)
from flask import Flask, request, jsonify
import secrets, time
app=Flask(__name__)
users={'alice@example.com':'oldpass'}
tokens={}
@app.route('/request-reset',methods=['POST'])
def request_reset():
    email=request.form.get('email')
    if email not in users: return 'OK'
    t=secrets.token_urlsafe(16); tokens[t]=(email,time.time()+3600)
    return jsonify({'token':t})
@app.route('/perform-reset',methods=['POST'])
def perform_reset():
    t=request.form.get('token'); new=request.form.get('new_password')
    info=tokens.get(t)
    if not info or info[1]<time.time(): return 'invalid',400
    users[info[0]]=new; del tokens[t]; return 'changed'
if __name__=='__main__': app.run(debug=True)
