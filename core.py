import sqlite3

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()

def searchRoute(start_Station, end_Station, date, time):
    return None

def populateDB():
  
  # Resetter tabellen
  cursor.execute('''DELETE FROM Banestrekning''')
  cursor.connection.commit()

  # Resetter tabellen
  cursor.execute('''DELETE FROM Stasjon''')
  cursor.connection.commit()

  # Resetter tabellen
  cursor.execute('''DELETE FROM Delstrekning''')
  cursor.connection.commit()

  # Resets Table
  cursor.execute('''DELETE FROM Togrute''')
  cursor.connection.commit() 

  # Setter inn informasjon om Banestrekninger
  cursor.execute('''INSERT INTO Banestrekning VALUES ('1', 'Nordlandsbanen', 'Diesel')''')
  cursor.execute('''INSERT INTO Banestrekning VALUES ('2', 'Dovrebanen', 'Elektrisk')''')
  cursor.execute('''INSERT INTO Banestrekning VALUES ('3', 'Bergensbanen', 'Elekstrisk')''')
  cursor.execute('''INSERT INTO Banestrekning VALUES ('4','Sørlandsbanen', 'Diesel')''')
  cursor.execute('''INSERT INTO Banestrekning VALUES ('5','Rørosbanen', 'Diesel')''')

  # Setter inn informasjon om Stasjoner
  cursor.execute('''INSERT INTO Stasjon VALUES ('Trondheim', 5.1)''')
  cursor.execute('''INSERT INTO Stasjon VALUES ('Steinskjer', 3.6)''')
  cursor.execute('''INSERT INTO Stasjon VALUES ('Mosjøen', 6.8)''')
  cursor.execute('''INSERT INTO Stasjon VALUES ('Mo i Rana', 3.5)''')
  cursor.execute('''INSERT INTO Stasjon VALUES ('Fauske', 34.0)''')
  cursor.execute('''INSERT INTO Stasjon VALUES ('Bodø', 4.1)''')

  # Setter inn informasjon om Delstrekninger
  cursor.execute('''INSERT INTO Delstrekning VALUES (1, 120, 1, 1, 'Trondheim', 'Steinskjer')''')
  cursor.execute('''INSERT INTO Delstrekning VALUES (2, 280, 0, 1, 'Steinskjer', 'Mosjøen')''')
  cursor.execute('''INSERT INTO Delstrekning VALUES (3, 90, 0, 1, 'Mosjøen', 'Mo i Rana')''')
  cursor.execute('''INSERT INTO Delstrekning VALUES (4, 170, 0, 1, 'Mo i Rana', 'Fauske')''')
  cursor.execute('''INSERT INTO Delstrekning VALUES (5, 60, 0, 1, 'Fauske', 'Bodø')''')


  cursor.connection.commit()
        
  
