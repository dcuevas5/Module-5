# vulnerable.py - Broken Access Control (no auth)
from flask import Flask, jsonify
app = Flask(__name__)
users = {"1":{"id":"1","name":"Alice"},"2":{"id":"2","name":"Bob"},"3":{"id":"3","name":"Admin","role":"admin"}}
@app.route('/account/<user_id>')
def get_account(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error":"Not found"}), 404
    return jsonify(user)
if __name__=='__main__':
    app.run(debug=True)
