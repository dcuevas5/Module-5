# vulnerable.py - simulated NoSQL injection (naive query)
users = [{'username':'alice'},{'username':'bob'},{'username':'admin'}]
def find(q):
    # assume q is a dict directly used as filter (unsafe)
    return [u for u in users if all(u.get(k)==v for k,v in q.items())]
if __name__=='__main__':
    print(find({'username':'alice'}))
