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
  #(BanestrekningID TEXT NOT NULL PRIMARY KEY,
	#BanestrekningNavn	TEXT NOT NULL,
	#Fremdriftsenergi TEXT NOT NULL)''')

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

"""

# Creates table Banestrekning
cursor.execute('''CREATE TABLE Banestrekning 
  #(BanestrekningID TEXT NOT NULL PRIMARY KEY,
	#BanestrekningNavn	TEXT NOT NULL,
	#Fremdriftsenergi TEXT NOT NULL)''')

cursor.connection.commit()

#cursor.execute("SELECT * FROM Banestrekning")
#rows = cursor.fetchall()
#print("All rows from table Banestrekning:")
#print(rows)

con.close()
