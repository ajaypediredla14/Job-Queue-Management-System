#database file

import sqlite3

conn=sqlite3.connect('data2.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
	email TEXT NOT NULL,
    subject TEXT,
    message TEXT 
	);''')


def show():
    query = "SELECT * FROM todo;"
    rows=conn.execute(query)
    return rows

def insertdata(email,subject,message):
    rs=conn.cursor()
    query = "INSERT INTO todo(email,subject,message) VALUES(?,?,?)"
    record=(email,subject,message)
    rs.execute(query,record)
    conn.commit()



def deletebytask(taskval):
    query = "DELETE FROM todo WHERE email = ? AND subject=? AND message=?;"
    conn.execute(query,taskval)
    conn.commit()


