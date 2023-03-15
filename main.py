import initDB
import sqlite3
from core import populateDB

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()

# Insert data for the Nordlandsbanen route
cursor.execute("INSERT INTO Banestrekning (BanestrekningID, BanestrekningNavn, Fremdriftenergi) VALUES ('1', 'Nordlandsbanen', 'Diesel')")

"""
cursor.execute("SELECT * FROM Banestrekning")
rows = cursor.fetchall()
print("All rows from table Banestrekning:")
print(rows)
"""
#Save changes to database
con.commit()
#Close connection to database
con.close()
