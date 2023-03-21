import sqlite3
from prettytable import PrettyTable
from initDB import initDB
from inputFunctions import start_station, end_station, date, time, get_phone_number, get_e_mail, get_name

# Creates a connection to our database
con = sqlite3.connect("TogDB.db")
# Creates a connecting object to our database
cursor = con.cursor()
# Read SQL script from file
initDB()

def populateDB():

    # Reset the database
    cursor.execute("DELETE FROM Banestrekning")
    cursor.execute("DELETE FROM Stasjon")
    cursor.execute("DELETE FROM Delstrekning")
    cursor.execute("DELETE FROM Togrute")
    con.commit()

    # Insert information about Banestrekninger
    cursor.execute(
        "INSERT INTO Banestrekning VALUES (2, 'Dovrebanen', 'Elektrisk')")
    cursor.execute(
        "INSERT INTO Banestrekning VALUES (3, 'Bergensbanen', 'Elekstrisk')")
    cursor.execute(
        "INSERT INTO Banestrekning VALUES (4,'Sørlandsbanen', 'Diesel')")
    cursor.execute(
        "INSERT INTO Banestrekning VALUES (5,'Rørosbanen', 'Diesel')")

    # Insert information about Stasjoner
    cursor.execute("INSERT INTO Stasjon VALUES ('Trondheim', 5.1)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Steinskjer', 3.6)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Mosjøen', 6.8)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Mo i Rana', 3.5)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Fauske', 34.0)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Bodø', 4.1)")

    # Insert information about Delstrekninger
    cursor.execute("INSERT INTO Delstrekning VALUES (1, 120, TRUE)")
    cursor.execute("INSERT INTO Delstrekning VALUES (2, 280, FALSE)")
    cursor.execute("INSERT INTO Delstrekning VALUES (3, 90, FALSE)")
    cursor.execute("INSERT INTO Delstrekning VALUES (4, 170, FALSE)")
    cursor.execute("INSERT INTO Delstrekning VALUES (5, 60, FALSE)")

    # commit changes
    con.commit()


def get_train_routes_for_station_on_weekday(StasjonNavn, Ukedag):
    con = sqlite3.connect("TogDB.db")
    cur = con.cursor()

    # get all train routes for the station
    cur.execute("""
        SELECT TogruteNavn
        FROM Rutestopp
        WHERE StasjonNavn = ?
    """, (StasjonNavn,))
    train_routes = cur.fetchall()

    # filter train routes by weekday
    filtered_train_routes = []
    for route in train_routes:
        cur.execute("""
            SELECT *
            FROM DatoerForTogruter
            WHERE Togrutenavn = ? AND strftime('%w', Dato) = ?
        """, (route[0], str(Ukedag)))
        if cur.fetchone():
            filtered_train_routes.append(route[0])

    con.close()

    return filtered_train_routes


def search_routes(start_station, end_station, date, time):
    conn = sqlite3.connect('TogDB.db')
    c = conn.cursor()

    # Construct the SQL query to join the Togrute and Rutestopp tables
    # to get all routes between the start and end stations
    query = """
        SELECT r.TogruteNavn, rs.Avgang, rs.Ankomst
        FROM Togrute r
        JOIN Rutestopp rs ON r.TogruteNavn = rs.TogruteNavn
        WHERE rs.StasjonNavn = ? AND r.TogruteNavn IN
            (SELECT TogruteNavn
             FROM Rutestopp
             WHERE StasjonNavn = ?)
    """

    def get_dates_for_togrute(cursor, togrute_navn):
        cursor.execute(
            "SELECT Dato FROM DatoerForTogruter WHERE Togrutenavn = ?", (togrute_navn,))
        dates = [row[0] for row in cursor.fetchall()]
        return dates

    # Get all the results and filter by date and time
    routes = []
    for row in c.execute(query, (start_station, end_station)):
        togrute_navn, avgang, ankomst = row
        if date in get_dates_for_togrute(c, togrute_navn) and avgang >= time:
            routes.append((togrute_navn, avgang, ankomst))

    # Sort the routes by time
    sorted_routes = sorted(routes, key=lambda x: x[1])

    conn.close()

    # Print the results in a table format
    if sorted_routes:
        table = PrettyTable()
        table.field_names = ['Train Route', 'Departure Time', 'Arrival Time']
        for route in sorted_routes:
            table.add_row(route)
        print(table)
    else:
        print("No routes found.")

    return sorted_routes


def search_routes_menu():
    print("\nSearch Routes")
    start = start_station()
    end = end_station()
    d = date()
    t = time()
    routes = search_routes(start, end, d, t)
    return routes


def register_user():
    con = sqlite3.connect("TogDB.db")
    cursor = con.cursor()
    print("\n Register as a user")
    cursor.execute("SELECT COUNT(*) from Kunde")
    KundeID=cursor.fetchone()[0]+1
    cursor.execute(""" 
    INSERT INTO Kunde(KundeID, Navn, Epost, Nummer)
    VALUES (?,?,?,?)      
    """, (KundeID, get_name(), get_e_mail(), get_phone_number()))
    con.commit()
    print("new user added")
    con.close
