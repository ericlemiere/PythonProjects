
import sqlite3

conn = sqlite3.connect('db_assignment.db')


#Create a table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()


#File list tuple
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')


for fileName in fileList:
    if fileName.endswith('txt'):
        with conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO tbl_files (file_name) VALUES (?)", (fileName,))
            print(fileName)


conn.close()




