import sqlite3


# Make the connection and create DB
conn = sqlite3.connect(":memory:")



with conn:
    cur = conn.cursor()
    cur.execute("DROP TABLE if exists tbl_Roster;")

# Create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists tbl_Roster( \
                col_Name TEXT, \
                col_Species TEXT, \
                col_IQ INT \
                );")
    conn.commit()


# Fill table
with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_Roster VALUES \
                ('Jean Baptiste','Human',122),\
                ('Korben Dallas','Alien',100),\
                ('Aknot', 'Mangalore', 5) \
                ;")
    conn.commit()




# Update table
with conn:
    cur = conn.cursor()
    cur.execute("UPDATE tbl_Roster SET col_Species = 'Human' \
                WHERE col_Name = 'Korben Dallas' \
                ;")
    conn.commit()


# Display Humans from table
with conn:
    cur = conn.cursor()
    cur.execute("SELECT col_Name, col_Species, col_IQ FROM tbl_Roster \
                WHERE col_Species = 'Human'")
    while True:
        row = cur.fetchone()
        if row is None:
            break
        print(row)

    
