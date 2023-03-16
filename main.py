import sqlite3
from inputFunctions import get_station_name, get_weekday
from core import get_train_routes_for_station_on_weekday, populateDB, search_routes

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
togruterows = cursor.fetchall()
print("All rows from table Togrute:")
print(togruterows)


station_name = get_station_name()
weekday = get_weekday()
# call function to get routes
routes = get_train_routes_for_station_on_weekday(station_name, weekday)

# print results
print(f"\nThe following routes stop at {station_name} on weekday number {weekday}:")
for route in routes:
    print(f"Route {route[0]} from {route[1]} to {route[2]}")

# Define the menu option for searching routes
def search_routes_menu():
    print("\nSearch Routes")
    start_station = input("Enter starting station: ")
    end_station = input("Enter ending station: ")
    date = input("Enter date (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM): ")
    routes = search_routes(start_station, end_station, date, time)
    if len(routes) == 0:
        print("No routes found.")
    else:
        print("Routes found:")
        for route in routes:
            print(f"- Train route: {route[0]}, Departure time: {route[1]}, Arrival time: {route[2]}")


#Save changes to database
con.commit()
#Close connection to database
con.close()
