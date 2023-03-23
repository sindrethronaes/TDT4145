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

    # USER STORY a)
    cursor.execute(
        "INSERT INTO Banestrekning VALUES (1, 'Nordlandsbanen', 'Diesel')")

    # Inserts information regarding Banestrekninger
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

    # USER STORY b)
    # Insert data for day train from Trondheim to Bodø into Togrute and Rutestopp
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn, DelstrekningID) VALUES ('dagtog fra trondheim til bodø', 1)")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Trondheim S', '07:49', 'NULL')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Steinkjer', '09:51', '09:51')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Mosjøen', '13:20', '13:20')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Mo i Rana', '14:31', '14:31')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Fauske', '16:49', '16:49')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('dagtog fra trondheim til bodø', 'Bodø', 'NULL', '17:34')")

    # USER STORY b)
    # Insert data for night train fra Trondheim to Bodø into Togrute and Rutestopp
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn, DelstrekningID) VALUES ('nattog fra Trondheim til Bodø', 1)")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Trondheim S', '23:05', 'NULL')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Steinkjer', '00:57', '00:57')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Mosjøen', '04:41', '04:41')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Mo i Rana', '05:55', '05:55')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Fauske', '08:19', '08:19')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('nattog fra Trondheim til Bodø', 'Bodø', 'NULL', '09:05')")

    # USER STORY b)
    # Inserts data for morning train from Mo i Rana to Trondheim into Togrute and Rutestopp
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn, DelstrekningID) VALUES ('morgentog fra Mo i Rana til Trondheim', 2)")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Mo i Rana', '08:11', 'NULL')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Mosjøen', '09:14', '09:14')")
    cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Steinkjer', '12:31', '12:31')")
    cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Trondheim S', 'NULL', '14:13')")

    # USER STORY f)
    # Inserts information regarding Operatører
    cursor.execute(
        "INSERT INTO Operatoer(OperatoerNavn, Banestrekning) VALUES ('VY AS', 'Nordlandsbanen')")
    cursor.execute(
        "INSERT INTO Operatoer(OperatoerNavn, Banestrekning) VALUES ('SJ Norge AS', 'Nordlandsbanen')")

    # Inserts information regarding DelstrekningIHovedretning
    cursor.execute(
        "INSERT INTO DelstrekningIHovedretning(DelstrekningID, Startstasjon, Endestasjon) VALUES (1, 'Trondheim', 'Steinkjer')")
    cursor.execute(
        "INSERT INTO DelstrekningIHovedretning(DelstrekningID, Startstasjon, Endestasjon) VALUES (2, 'Steinkjer', 'Mosjøen')")
    cursor.execute(
        "INSERT INTO DelstrekningIHovedretning(DelstrekningID, Startstasjon, Endestasjon) VALUES (3, 'Mosjøen', 'Mo i Rana')")
    cursor.execute(
        "INSERT INTO DelstrekningIHovedretning(DelstrekningID, Startstasjon, Endestasjon) VALUES (4, 'Mo i Rana', 'Fauske')")
    cursor.execute(
        "INSERT INTO DelstrekningIHovedretning(DelstrekningID, Startstasjon, Endestasjon) VALUES (5, 'Fauske', 'Bodø')")

    # Inserts information regarding TogruterPåBanestrekning
    cursor.execute(
        "INSERT INTO TogruterPaaBanestrekning(Banestrekning, TogruteNavn) VALUES ('Nordlandsbanen', 'VY AS')")
    cursor.execute(
        "INSERT INTO TogruterPaaBanestrekning(Banestrekning, TogruteNavn) VALUES ('Nordlandsbanen', 'SJ Norge AS')")

    # Inserts information regarding Dato
    cursor.execute(
        "INSERT INTO Dato(Dato, Ukedag) VALUES ('2023-04-03', 'Mandag')")
    cursor.execute(
        "INSERT INTO Dato(Dato, Ukedag) VALUES ('2023-04-04', 'Tirsdag')")

    # Inserts information regarding Vogn, Sovevogn, Sittevogn (10 of each)
    for i in range(1, 11):
        cursor.execute("INSERT INTO Vogn(VognID, Navn, TilgjengeligForBruk, NummerIVognsammensetning, VognType, OperatørNavn) VALUES (?, 'Sittevogn', 'Ledig', 'NULL', 'SJ-sittevogn-1', 'SJ Norge AS' )", (i,))

    for i in range(11, 21):
        cursor.execute(f"INSERT INTO Vogn(VognID, Navn, TilgjengeligForBruk, NummerIVognsammensetning, VognType, OperatørNavn) VALUES (?, 'Sovevogn', 'Ledig', 'NULL', 'SJ-sovevogn-1', 'SJ Norge AS' )", (i,))

    # Inserts information regarding seats (12 seats per car)
    for i in range(1, 11):
        for j in range(1, 13):
            cursor.execute(
                "INSERT INTO Sittevogn(VognID, AntallSeter, SeterPerVogn) VALUES (?, ?, 12)", (i, j))

    # Inserts information regarding beds (8 beds per car)
    for i in range(11, 21):
        for j in range(1, 9):
            cursor.execute(
                "INSERT INTO Sovevogn(VognID, AntallSenger, SengerPerKupe) VALUES (?, ?, 2)", (i, j))

    # Inserts information regarding Kupe
    for i in range(11, 21):
        for j in range(1, 5):
            cursor.execute(
                "INSERT INTO Kupe(KupeID, VognID, AntallSenger, Tilgjengelig) VALUES (?, ?, 8 , 'Ja')", (j, i))

    # Inserts information regarding Seng (8 Beds in total per Kupe)
    for k in range(11, 21):
        for i in range(1, 5):
            for j in range(1, 3):
                cursor.execute(
                    "INSERT INTO Seng(SengID, KupeID, VognID, Tilgjengelig) VALUES (?, ?, ?, 'Ja')", (j, i, k))

    # Inserts information regarding Sete (12 Seats in total per Vogn)
    for i in range(1, 11):
        for j in range(1, 13):
            cursor.execute(
                "INSERT INTO Sete(SeteID, VognID, Tilgjengelig) VALUES (?, +, 'Ja')", (j, i))

    # Commit the changes aka "Saves" the DB-State
    con.commit()


def get_train_routes_for_station_on_weekday(station_name, weekday):
    """ 
    This function returns all train routes that passes a given station 
    on a given day of the week. Necessary for user story c).

    Parameters
    ----------
    station_name : string
      The name of the station
    weekday : string 
      The name of the weekday

    Returns
    -------
    List[string]
      A list consisting of train routes
    """

    con = sqlite3.connect("TogDB.db")
    cur = con.cursor()

    # Gets all train routes for the station
    cur.execute("""
        SELECT TogruteNavn
        FROM Rutestopp
        WHERE StasjonNavn = ?
    """, (station_name,))
    train_routes = cur.fetchall()

    # Filter train routes by weekday
    filtered_train_routes = []
    for route in train_routes:
        # NB! IS '%w' GOOD PRATICE REF. #3 in python-sqlite.pdf?
        cur.execute("""
            SELECT *
            FROM DatoerForTogruter
            WHERE Togrutenavn = ? AND strftime('%w', Dato) = ?
        """, (route[0], str(weekday)))
        if cur.fetchone():
            filtered_train_routes.append(route[0])

    # Good practice to close the DB
    con.close()

    # Returns all train routes that passes the given station on the given day of the week
    return filtered_train_routes



def search_routes(start_station, end_station, date, time):
    """
    This function returns all train routes that occurs on a given date and time in between
    a start station and and end station. Necessary for user story d).

    Parameters
    ----------
    start_station : string
      The name of the start station
    end_station : string
      The name of the end station

    Returns
    -------
    List[string]
      A list consisting of train routes
    """

    conn = sqlite3.connect('TogDB.db')
    c = conn.cursor()

    # Constructs the SQL query to join the Togrute and Rutestopp tables
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



def get_dates_for_togrute(cursor, togrute_navn):
    """
    This function returns all dates of departure for a given train route

    Parameters
    ----------
    cursor : cursor
      A cursor object that allows access to the DB
    togrute_navn : string
      The name of given train route

    Returns
    -------
    List[string]
      A list consisting of dates
    """
    # Execute script for retrieving all dates related to a given train route
    cursor.execute(
        "SELECT Dato FROM DatoerForTogruter WHERE Togrutenavn = ?", (togrute_navn,))

    # All first rows are dates for the given train route
    dates = [row[0] for row in cursor.fetchall()]

    # Return all dates
    return dates


def check_user_story_a():
    """This function is used to test user story a)"""

    cursor.execute("SELECT * FROM Banestrekning")
    banestrekningrows = cursor.fetchall()
    print("All rows from table Banestrekning:")
    for banestrekning in banestrekningrows:
        print(banestrekning)


def check_user_story_b():
    """This function is used to test user story b)"""

    cursor.execute("SELECT * FROM Togrute")
    togruterows = cursor.fetchall()
    print("All rows from table Togrute:")
    for togrute in togruterows:
        print(togrute)


def check_user_story_f():
    pass
