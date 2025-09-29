# fixed.py - safe handling: enforce types and allowlist
users = [{'username':'alice'},{'username':'bob'},{'username':'admin'}]
def find_username(value):
    if not isinstance(value,str): raise ValueError('invalid')
    return [u for u in users if u.get('username')==value]
if __name__=='__main__':
    print(find_username('alice'))
