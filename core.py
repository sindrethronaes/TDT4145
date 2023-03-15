import sqlite3
from initDB import initDB

# Creates a connection to our database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()
# Read SQL script from file
initDB()

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

def get_train_routes_for_station_on_weekday(station_name, weekday):
    con = sqlite3.connect("TogDB.db")
    cur = con.cursor()

    # get all train routes for the station
    cur.execute("""
        SELECT TogruteNavn
        FROM Rutestopp
        WHERE StasjonNavn = ?
    """, (station_name,))
    train_routes = cur.fetchall()

    # filter train routes by weekday
    filtered_train_routes = []
    for route in train_routes:
        cur.execute("""
            SELECT *
            FROM DatoerForTogruter
            WHERE Togrutenavn = ? AND strftime('%w', Dato) = ?
        """, (route[0], str(weekday)))
        if cur.fetchone():
            filtered_train_routes.append(route[0])

    con.close()

    return filtered_train_routes