import sqlite3

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")

# Read SQL script from file
with open('Jernbane.sql', 'r') as f:
    sql_script = f.read()


con.executescript(sql_script)

con.commit()
con.close()