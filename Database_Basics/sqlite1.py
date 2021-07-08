
import sqlite3

conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_persons( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fname TEXT, \
        col_lname TEXT, \
        col_email TEXT \
        )")
    conn.commit()
conn.close()





conn = sqlite3.connect('test.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
        VALUES (?,?,?)", \
                ('Bob','Smith','bob@bobsmith.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
        VALUES (?,?,?)", \
                ('Sue','Smith','sue@bobsmith.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
        VALUES (?,?,?)", \
                ('Ryan','Smith','ryan@bobsmith.com'))
    cur.execute("INSERT INTO tbl_persons(col_fname, col_lname, col_email) \
        VALUES (?,?,?)", \
                ('Julie','Smith','julie@bobsmith.com'))
    conn.commit()
conn.close()



conn = sqlite3.connect('test.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_fname, col_lname, col_email FROM tbl_persons \
        WHERE col_fname = 'Sue'")
    varPerson = cur.fetchall()
    for item in varPerson:
        msg = "First Name: {}\nLast Name: {}\nEmail: {}".format(item[0],item[1],item[2])
    print(msg)
