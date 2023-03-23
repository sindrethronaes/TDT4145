import sqlite3
from prettytable import PrettyTable
from initDB import initDB
from inputFunctions import *

# Creates a connection to our database
con = sqlite3.connect("TogDB.db")

# Creates a connecting object to our database
cursor = con.cursor()

# Read SQL script from file
initDB()


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
    date : string
        The date in the format YYYY-MM-DD
    time : string
        The time in the format HH:MM

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

    return sorted_routes if sorted_routes else []



def check_user_story_a():
    #This function is used to test user story a)

    cursor.execute("SELECT * FROM Banestrekning")
    banestrekningrows = cursor.fetchall()
    print("All rows from table Banestrekning:")
    for banestrekning in banestrekningrows:
        print(banestrekning)


def check_user_story_b():
    #This function is used to test user story b)

    cursor.execute("SELECT * FROM Togrute")
    togruterows = cursor.fetchall()
    print("All rows from table Togrute:")
    for togrute in togruterows:
        print(togrute)

def check_user_story_c():
    #This function is used to test user story c)

    station_name = get_station_name()
    weekday = get_weekday()

    # print results
    print(
        f"\nThe following routes stop at {station_name} on weekday number {weekday}:")

def check_user_story_d():
    print("\nSearch Routes")
    start = start_station()
    end = end_station()
    d = date()
    t = time()
    routes = search_routes(start, end, d, t)
    return routes

def check_user_story_e():
    pass

def check_user_story_f():
    pass

def check_user_story_g():
    pass

# Run python main.py purchases <customer_id> in the terminal to see the upcoming purchases for a customer
def check_user_story_h():
    pass
