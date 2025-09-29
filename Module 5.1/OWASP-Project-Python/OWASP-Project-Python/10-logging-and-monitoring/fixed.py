# fixed.py - basic logging
import logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
def login(u,p):
    if u=='admin' and p=='secret':
        logging.info('login success %s', u); return True
    logging.warning('failed login %s', u); return False
if __name__=='__main__': print(login('admin','bad'))
