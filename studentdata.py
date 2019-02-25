import sqlite3

conn = sqlite3.connect('student123.db')
c = conn.cursor()

def ct2():
    c.execute('create table std1(sno text,sname text,dept ,Totalmarks integer )')
def ins2():
    c.execute("insert into std1 values ('012','Arpan','civil',100)")
    c.execute("insert into std1 values ('022','Arpan1','computer science',200)")
    c.execute("insert into std1 values ('032','Arpan2','Mechanical Engineering',300)")
    c.execute("insert into std1 values ('033','Arpan3','Electrical',400)")
    c.execute("insert into std1 values ('034','Arpan4','Medical',500)")
    conn.commit()
def ft2():
    c.execute("select * from std1")
    data = c.fetchall()
    print(data)
#ct2()
#ins2()
ft2()
c.close()
conn.close()