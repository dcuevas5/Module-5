# vulnerable.py - external script without integrity
html='''<html><head></head><body><script src="https://cdn.example.com/lib.js"></script></body></html>'''
if __name__=='__main__': print(html)
