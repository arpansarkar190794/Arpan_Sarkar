import sqlite3

conn = sqlite3.connect('emp123.db')
c = conn.cursor()

def ct1():
    c.execute('create table tcs1(empno text,empname text,salary integer ,department text)')
def ins1():
    c.execute("insert into tcs1 values ('012','Arpan',50000,'civil')")
    c.execute("insert into tcs1 values ('022','Arpan1',50000,'computer science')")
    c.execute("insert into tcs1 values ('032','Arpan2',50000,'Mechanical Engineering')")
    c.execute("insert into tcs1 values ('033','Arpan3',50000,'Electrical')")
    c.execute("insert into tcs1 values ('034','Arpan4',50000,'Medical')")
    conn.commit()
def ft1():
    c.execute("select * from tcs1")
    data = c.fetchall()
    print(data)
ct1()
ins1()
ft1()
c.close()
conn.close()