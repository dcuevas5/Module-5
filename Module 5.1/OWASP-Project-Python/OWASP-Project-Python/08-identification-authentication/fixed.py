# fixed.py - bcrypt usage
import bcrypt
def hash_pw(p): return bcrypt.hashpw(p.encode(), bcrypt.gensalt())
def check_pw(p,h): return bcrypt.checkpw(p.encode(), h)
if __name__=='__main__':
    h=hash_pw('password123'); print(check_pw('password123',h))
