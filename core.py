import sqlite3
from initDB import initDB

# Creates a connection to our database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()
# Read SQL script from file
initDB()

def searchRoute(start_Station, end_Station, date, time):
    return None

def populateDB():
  
  # Resetter alle tabeller i DB
  cursor.execute("DELETE FROM Banestrekning")
  cursor.execute("DELETE FROM Stasjon")
  cursor.execute("DELETE FROM Delstrekning")
  cursor.execute("DELETE FROM Togrute")
  con.commit() 

  # Setter inn informasjon om Banestrekninger
  cursor.execute("INSERT INTO Banestrekning VALUES (2, 'Dovrebanen', 'Elektrisk')")
  cursor.execute("INSERT INTO Banestrekning VALUES (3, 'Bergensbanen', 'Elekstrisk')")
  cursor.execute("INSERT INTO Banestrekning VALUES (4,'Sørlandsbanen', 'Diesel')")
  cursor.execute("INSERT INTO Banestrekning VALUES (5,'Rørosbanen', 'Diesel')")

  # Setter inn informasjon om Stasjoner
  cursor.execute("INSERT INTO Stasjon VALUES ('Trondheim', 5.1)")
  cursor.execute("INSERT INTO Stasjon VALUES ('Steinskjer', 3.6)")
  cursor.execute("INSERT INTO Stasjon VALUES ('Mosjøen', 6.8)")
  cursor.execute("INSERT INTO Stasjon VALUES ('Mo i Rana', 3.5)")
  cursor.execute("INSERT INTO Stasjon VALUES ('Fauske', 34.0)")
  cursor.execute("INSERT INTO Stasjon VALUES ('Bodø', 4.1)")

  # Setter inn informasjon om Delstrekninger
  cursor.execute("INSERT INTO Delstrekning VALUES (1, 120, TRUE)")
  cursor.execute("INSERT INTO Delstrekning VALUES (2, 280, FALSE)")
  cursor.execute("INSERT INTO Delstrekning VALUES (3, 90, FALSE)")
  cursor.execute("INSERT INTO Delstrekning VALUES (4, 170, FALSE)")
  cursor.execute("INSERT INTO Delstrekning VALUES (5, 60, FALSE)")

  # commit changes
  con.commit()
        
  
