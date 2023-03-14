import sqlite3

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()

""""
cursor.execute("SELECT * FROM person WHERE navn = ?", (navn))
cursor.execute("SELECT * FROM person")
row = cursor.fetchone()
print("First row from table person:")
print(row)

cursor.execute("SELECT * FROM person")
rows = cursor.fetchall()
print("All rows in the table person:")
print(rows)

cursor.execute("SELECT * FROM person")
rows = cursor.fetchmany(2)
print("First two rows from table person:")
print(rows)

for row in cursor.execute("SELECT * FROM person"):
print(row)

cursor.execute('''CREATE TABLE person
(id INTEGER PRIMARY KEY, name TEXT, birthday TEXT)''')
cursor.execute('''INSERT INTO person VALUES (1, 'Ola Nordmann', '2002-02-02')''')
connection.commit()
connection.close()

"""

"""
# Creates table Banestrekning
cursor.execute('''CREATE TABLE Banestrekning 
  (BanestrekningID TEXT NOT NULL PRIMARY KEY,
	BanestrekningNavn	TEXT NOT NULL,
	Fremdriftsenergi TEXT NOT NULL)''')

# Inserts information about Banestrekning
cursor.execute(
    '''DELETE FROM Banestrekning''')
cursor.connection.commit()
cursor.execute(
    '''INSERT INTO Banestrekning VALUES ('1', 'Nordlandsbanen', 'Diesel')''')
cursor.execute(
    '''INSERT INTO Banestrekning VALUES ('2', 'Dovrebanen', 'Elektrisk')''')
cursor.execute(
    '''INSERT INTO Banestrekning VALUES ('3', 'Bergensbanen', 'Elekstrisk')''')
cursor.execute(
    '''INSERT INTO Banestrekning VALUES ('4','Sørlandsbanen', 'Diesel')''')
cursor.execute(
    '''INSERT INTO Banestrekning VALUES ('5','Rørosbanen', 'Diesel')''')

# Creates table togrute
cursor.execute('''CREATE TABLE Togrute
  ("TogruteNavn"	TEXT NOT NULL PRIMARY KEY,
	"DelstrekningID"	TEXT NOT NULL REFERENCES DelstrekningIHovedretning(DelstrekningID))''')
"""

# Creates table Stasjon
cursor.execute('''CREATE TABLE Stasjon
    ("StasjonNavn"	TEXT NOT NULL PRIMARY KEY,
    "Moh"	FLOAT NOT NULL)''')

cursor.execute('''INSERT INTO Stasjon VALUES ('Trondheim', 5.1)''')
cursor.execute('''INSERT INTO Stasjon VALUES ('Steinskjer', 3.6)''')
cursor.execute('''INSERT INTO Stasjon VALUES ('Mosjøen', 6.8)''')
cursor.execute('''INSERT INTO Stasjon VALUES ('Mo i Rana', 3.5)''')
cursor.execute('''INSERT INTO Stasjon VALUES ('Fauske', 34.0)''')
cursor.execute('''INSERT INTO Stasjon VALUES ('Bodø', 4.1)''')

# Creates table Delstrekning
cursor.execute('''CREATE TABLE Delstrekning(
    "DelstrekningID"	INT NOT NULL PRIMARY KEY,
    "LengdeIKM" INT NOT NULL,
    "HarDobbeltSpor" BOOLEAN NOT NULL,
    "BanestrekningID"	INT NOT NULL REFERENCES Banestrekning(BanestrekningID),
    "StartStasjon"	TEXT NOT NULL REFERENCES Stasjon(StasjonNavn),
    "EndeStasjon"    TEXT NOT NULL REFERENCES Stasjon(StasjonNavn))''')

cursor.execute('''INSERT INTO Delstrekning VALUES (1, 120, 1, 1, 'Trondheim', 'Steinskjer')''')
cursor.execute('''INSERT INTO Delstrekning VALUES (2, 280, 0, 1, 'Steinskjer', 'Mosjøen')''')
cursor.execute('''INSERT INTO Delstrekning VALUES (3, 90, 0, 1, 'Mosjøen', 'Mo i Rana')''')
cursor.execute('''INSERT INTO Delstrekning VALUES (4, 170, 0, 1, 'Mo i Rana', 'Fauske')''')
cursor.execute('''INSERT INTO Delstrekning VALUES (5, 60, 0, 1, 'Fauske', 'Bodø')''')



cursor.connection.commit()

cursor.execute("SELECT * FROM Banestrekning")
rows = cursor.fetchall()
print("All rows from table Banestrekning:")
print(rows)

con.close()
