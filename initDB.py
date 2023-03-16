import sqlite3

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()

cursor.executescript("Jernbane.sql")

"""
# Lager tabellen Banestrekning
cursor.execute('''CREATE TABLE Banestrekning (BanestrekningID TEXT NOT NULL PRIMARY KEY, BanestrekningNavn	TEXT NOT NULL, Fremdriftsenergi TEXT NOT NULL)''')

# Lager tabellen stasjon
cursor.execute('''CREATE TABLE Stasjon ("StasjonNavn"	TEXT NOT NULL PRIMARY KEY, "Moh"	FLOAT NOT NULL)''')

# Lager tabellen Delstrekning
cursor.execute('''CREATE TABLE Delstrekning("DelstrekningID"	INT NOT NULL PRIMARY KEY, "LengdeIKM" INT NOT NULL, "HarDobbeltSpor" BOOLEAN NOT NULL, "BanestrekningID"	INT NOT NULL REFERENCES Banestrekning(BanestrekningID), "StartStasjon" TEXT NOT NULL REFERENCES Stasjon(StasjonNavn), "EndeStasjon" TEXT NOT NULL REFERENCES Stasjon(StasjonNavn))''')

# Creates table Togrute
cursor.execute('''CREATE TABLE Togrute ("TogruteNavn"	TEXT NOT NULL PRIMARY KEY, "Avgangstid" DATETIME NOT NULL, "Ankomststid" DATETIME NOT NULL, "Startstasjon"	TEXT NOT NULL REFERENCES Stasjon(StasjonNavn), "Endestasjon" TEXT NOT NULL REFERENCES Stasjon(StasjonNavn))''')

"""

cursor.connection.commit()