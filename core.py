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
    # call function to get routes
    routes = check_user_story_c(station_name, weekday)

    # print results
    print(
        f"\nThe following routes stop at {station_name} on weekday number {weekday}:")
    for route in routes:
        print(f"Route {route[0]} from {route[1]} to {route[2]}")

# Run python main.py purchases <customer_id> in the terminal to see the upcoming purchases for a customer
def check_user_story_h(customer_id):
    with sqlite3.connect("TogDB.db") as conn:
        c = conn.cursor()
        c.execute("""SELECT t.date, r.name, t.departure_time, t.arrival_time, t.price
                     FROM purchases p
                     JOIN tickets t ON t.id = p.ticket_id
                     JOIN routes r ON r.id = t.route_id
                     WHERE p.customer_id = ?
                     AND t.departure_time > datetime('now')
                     ORDER BY t.departure_time ASC""", (customer_id,))
        rows = c.fetchall()
        if not rows:
            print("No upcoming purchases found for customer", customer_id)
            return
        table = PrettyTable(['Date', 'Route', 'Departure Time', 'Arrival Time', 'Price'])
        table.align['Route'] = 'l'
        for row in rows:
            table.add_row(row)
        print(table)

def check_user_story_d():
    print("\nSearch Routes")
    start = start_station()
    end = end_station()
    d = date()
    t = time()
    routes = search_routes(start, end, d, t)
    return routes

def check_user_story_e():
    con = sqlite3.connect("TogDB.db")
    cursor = con.cursor()
    print("\n Register as a user")
    cursor.execute("SELECT COUNT(*) from Kunde")
    KundeID=cursor.fetchone()[0]+1
    cursor.execute(""" 
    INSERT INTO Kunde(KundeID, Navn, Epost, Nummer)
    VALUES (?,?,?,?)      
    """, (KundeID, get_contact_info))
    con.commit()
    print("new user added")
    con.close

def check_user_story_f():
    pass
