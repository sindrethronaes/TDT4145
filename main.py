import initDB
import sqlite3

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()

"""
cursor.execute("SELECT * FROM Banestrekning")
rows = cursor.fetchall()
print("All rows from table Banestrekning:")
print(rows)
"""

con.close()
