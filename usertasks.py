#database file

import sqlite3

conn=sqlite3.connect('data2.db')
conn.execute('''CREATE TABLE IF NOT EXISTS todo(
	email TEXT NOT NULL,
    subject TEXT,
    message TEXT 
	);''')

#function to show pass the data to the populate(task_kinter.py) function 
def show():
    query = "SELECT * FROM todo;"
    rows=conn.execute(query)
    return rows

#function to insert the data to the database
def insertdata(email,subject,message):
    rs=conn.cursor()
    query = "INSERT INTO todo(email,subject,message) VALUES(?,?,?)"
    record=(email,subject,message)
    rs.execute(query,record)
    conn.commit()


#function to delete the task
def deletebytask(taskval):
    query = "DELETE FROM todo WHERE email = ? AND subject=? AND message=?;"
    conn.execute(query,taskval)
    conn.commit()


