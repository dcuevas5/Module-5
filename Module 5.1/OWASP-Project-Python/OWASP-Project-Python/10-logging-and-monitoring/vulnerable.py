# vulnerable.py - no logging
def login(u,p):
    if u=='admin' and p=='secret': return True
    return False
if __name__=='__main__': print(login('admin','bad'))
