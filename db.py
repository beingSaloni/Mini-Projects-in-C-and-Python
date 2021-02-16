import sqlite3

def createtable():
    conn = sqlite3.connect('lite.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE data(roll no INTEGER , name TEXT , marks REAL)")
    conn.commit()
    conn.close()


createtable()