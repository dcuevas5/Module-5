# vulnerable.py - insecure password reset
from flask import Flask, request
app=Flask(__name__)
users={'alice@example.com':'oldpass'}
@app.route('/reset-password',methods=['POST'])
def reset():
    email=request.form.get('email'); new=request.form.get('new_password')
    users[email]=new
    return 'ok'
if __name__=='__main__': app.run(debug=True)
