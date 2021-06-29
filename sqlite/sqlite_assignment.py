
import sqlite3
connection = sqlite3.connect("/Users/ericlemiere/Documents/GitHub/PythonProjects/sqlite/database.db")

c = connection.cursor() # this allows for communication across the connection

c.execute("CREATE TABLE IF NOT EXISTS People(FirstName TEXT, LastName TEXT, Age INT)")


c.execute("INSERT INTO People VALUES('Ron','Obvious',42)")
connection.commit()
