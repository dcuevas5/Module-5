# fixed.py - Broken Access Control (simple token auth simulation)
from flask import Flask, jsonify, request
app = Flask(__name__)
users = {"1":{"id":"1","name":"Alice","role":"user"},"2":{"id":"2","name":"Bob","role":"user"},"3":{"id":"3","name":"Admin","role":"admin"}}
def get_current_user():
    auth = request.headers.get('Authorization','')
    if auth.startswith('Bearer '):
        token = auth.split(' ',1)[1].strip()
        return users.get(token)
    return None
@app.route('/account/<user_id>')
def get_account(user_id):
    current = get_current_user()
    if not current:
        return jsonify({"error":"Authentication required"}), 401
    if current['id'] != user_id and current.get('role') != 'admin':
        return jsonify({"error":"Forbidden"}), 403
    user = users.get(user_id)
    if not user:
        return jsonify({"error":"Not found"}), 404
    return jsonify(user)
if __name__=='__main__':
    app.run(debug=True)
