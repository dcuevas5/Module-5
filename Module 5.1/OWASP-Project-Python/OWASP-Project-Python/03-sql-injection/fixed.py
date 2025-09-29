# fixed.py - parameterized queries
import sqlite3
conn=sqlite3.connect(':memory:');c=conn.cursor()
c.execute('create table users(id int,username text)')
c.execute("insert into users values(1,'alice')");c.execute("insert into users values(2,'bob')");conn.commit()
def find(u):
    q = "SELECT username FROM users WHERE username = ?"
    print('PARAM QUERY:',q)
    return c.execute(q,(u,)).fetchall()
if __name__=='__main__':
    print(find("bob' OR '1'='1"))
