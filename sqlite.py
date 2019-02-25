import sqlite3

conn = sqlite3.connect('test000.db')
c = conn.cursor()

def ct():
    c.execute('create table emp1(emp text,empname text)')
def ins():
    c.execute("insert into emp1 values ('007','Arpanyyy')")
    c.execute("insert into emp1 values ('0076','Argjggpanyyy')")
    c.execute("insert into emp1 values ('8007','Arpangjghyyy')")
    conn.commit()
def ft():
    c.execute("select * from emp1")
    data = c.fetchall()
    print(data[1])

#ct()
#ins()
ft()


c.close()
conn.close()



