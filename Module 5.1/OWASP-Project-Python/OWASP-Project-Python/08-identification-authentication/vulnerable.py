# vulnerable.py - plaintext password compare
def login(input_pw, stored_pw):
    return input_pw == stored_pw
if __name__=='__main__':
    print(login('pass','pass'))
