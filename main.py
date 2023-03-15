import sqlite3
from core import populateDB

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()
# Populate the database with data
populateDB()

# Insert data for Nordlandsbanen
cursor.execute("INSERT INTO Banestrekning (BanestrekningID, BanestrekningNavn, Fremdriftsenergi) VALUES (1, 'Nordlandsbanen', 'Diesel')")

# Insert data for the dagtog fra Trondheim til Bodø route
cursor.execute("INSERT INTO Togrute(TogruteNavn, DelstrekningID) VALUES ('dagtog fra trondheim til bodø', 1)")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Trondheim S', '07:49', 'NULL')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Steinkjer', '09:51', '09:51')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Mosjøen', '13:20', '13:20')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Mo i Rana', '14:31', '14:31')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Fauske', '16:49', '16:49')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Bodø', 'NULL', '17:34')")

# Insert data for the nattog fra Trondheim til Bodø route
cursor.execute("INSERT INTO Togrute(TogruteNavn, DelstrekningID) VALUES ('nattog fra Trondheim til Bodø', 1)")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Trondheim S', '23:05', 'NULL')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Steinkjer', '00:57', '00:57')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Mosjøen', '04:41', '04:41')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Mo i Rana', '05:55', '05:55')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Fauske', '08:19', '08:19')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Bodø', 'NULL', '09:05')")

# Insert data for the morgentog fra Mo i Rana til Trondheim route
cursor.execute("INSERT INTO Togrute(TogruteNavn, DelstrekningID) VALUES ('morgentog fra Mo i Rana til Trondheim', 2)")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Mo i Rana', '08:11', 'NULL')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Mosjøen', '09:14', '09:14')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Steinkjer', '12:31', '12:31')")
cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Trondheim S', 'NULL', '14:13')")


cursor.execute("SELECT * FROM Banestrekning")
banestrekningrows = cursor.fetchall()
print("All rows from table Banestrekning:")
print(banestrekningrows)

cursor.execute("SELECT * FROM Togrute")
togruterows = cursor.fetchmany(1)
print("All rows from table Togrute:")
print(togruterows)

#Save changes to database
con.commit()
#Close connection to database
con.close()