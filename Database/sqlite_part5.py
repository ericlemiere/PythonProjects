import sqlite3

firstName = input("Enter first name: ")
lastName = input("Enter last name: ")
age = int(input("Enter age: "))
personData = (firstName, lastName, age)




with sqlite3.connect("/Users/ericlemiere/Documents/GitHub/PythonProjects/Database/test_db.db") as connection:
    c = connection.cursor()
    c.executescript("DROP TABLE IF EXISTS People; \
            CREATE TABLE People(FirstName TEXT, LastName TEXT, Age INT); \
            INSERT INTO People VALUES('Ron','Obvious',42);")

    peopleValues = (('Luigi','Vercotti',43), ('Arthur','Belling',28))
    c.executemany("INSERT INTO People VALUES(?,?,?)", peopleValues)
    c.execute("INSERT INTO People VALUES (?,?,?)", personData)

    c.execute("UPDATE People SET Age=? WHERE FirstName=? AND LastName=?",
                  (45, 'Luigi', 'Vercotti'))

    c.execute("SELECT FirstName, LastName FROM People WHERE Age > 40")
    while True:
        row = c.fetchone()
        if row is None:
            break
        print(row)

