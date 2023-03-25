import sqlite3
from initDB import initDB
from inputFunctions import *

# Creates a connection to our database
con = sqlite3.connect("TogDB.db")

# Creates a connecting object to our database
cursor = con.cursor()

# Read SQL script from file
initDB()


def get_train_routes_by_station_and_day(station_name, day_of_week):
    cursor.execute("""
        SELECT TogRute.TogRuteNavn
        FROM TogRute, Rutestopp, Dato
        WHERE Rutestopp.StasjonNavn = ? AND
        TogRute.TogRuteNavn = Rutestopp.TogruteNavn AND
        TogRute.Dato = Dato.Dato AND
        Dato.Ukedag = ?;
    """, (station_name, f"%{day_of_week}%"))

    train_routes = cursor.fetchall()

    return train_routes


def get_train_routes(start_station, end_station, date, time):
    cursor.execute("""
        SELECT TogRute.TogruteNavn
        FROM Togrute, Rutestopp AS StartStopp, Rutestopp AS EndStopp
        WHERE StartStopp.StasjonNavn = ? AND
        EndStopp.StasjonNavn = ? AND
        Togrute.TogruteNavn = StartStopp.TogruteNavn AND
        Togrute.TogruteNavn = EndStopp.TogruteNavn AND
        StartStopp.Avgang >= ? AND
        StartStopp.Avgang < EndStopp.Ankomst AND
        Togrute.Dato BETWEEN ? AND ? + 1
        ORDER BY StartStopp.Avgang;
    """, (start_station, end_station, time, date, date))
    
    train_routes = cursor.fetchall()

    return train_routes

def register_user(name, e_mail, phone_number):
    con = sqlite3.connect("TogDB.db")
    cursor = con.cursor()
    print("\n Register as a user")
    cursor.execute("SELECT COUNT(*) from Kunde")
    KundeID = cursor.fetchone()[0]+1
    cursor.execute(""" 
    INSERT INTO Kunde(KundeID, Navn, Epost, Nummer)
    VALUES (?,?,?,?)      
    """, (KundeID, name, e_mail, phone_number))
    con.commit()
    print("new user added")


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


def check_user_story_c():
    """This function is used to test user story c)"""

    station_name = get_station_name()
    # You can use Norwegian days like "Mandag" if your data is in Norwegian
    day_of_week = get_weekday()
    train_routes = get_train_routes_by_station_and_day(
        station_name, day_of_week)
    print(f"Train routes passing through {station_name} on {day_of_week}:")
    for train_route in train_routes:
        print(train_route[0])


def check_user_story_d():
    """This function is used to test user story d)"""
    
    start_station = get_station_name()
    end_station = get_station_name()
    date = get_date()
    time = get_time()
    train_routes = get_train_routes(start_station, end_station, date, time)
    print(f"Train routes from {start_station} to {end_station} on {date} at {time}:")
    for train_route in train_routes:
        print(train_route[0])


def check_user_story_e():
    """This function is used to test user story e)"""
    name = get_name()
    e_mail = get_e_mail()
    phone_number = get_phone_number()
    register_user(name, e_mail, phone_number)

    cursor.execute("SELECT * FROM Kunde")
    kunderows = cursor.fetchall()
    print("All rows from table Kunde:")
    for kunde in kunderows:
        print(kunde)


def check_user_story_f():
    pass


def check_user_story_g():
    pass


def check_user_story_h():
    pass
