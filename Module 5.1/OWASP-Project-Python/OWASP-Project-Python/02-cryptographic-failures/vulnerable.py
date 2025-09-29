# vulnerable.py - insecure hashing (MD5)
import hashlib
def hash_md5(p): return hashlib.md5(p.encode()).hexdigest()
if __name__=='__main__':
    print('md5(password123)=', hash_md5('password123'))
