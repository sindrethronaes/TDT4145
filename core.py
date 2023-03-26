import sqlite3
from initDB import initDB
import datetime
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



def get_user_id_by_name_or_phone(name=None, phone=None):
    with sqlite3.connect("TogDB.db") as conn:
        cursor = conn.cursor()

        if name:
            query = 'SELECT KundeID FROM Kunde WHERE Navn = ?'
            cursor.execute(query, (name,))
        elif phone:
            query = 'SELECT KundeID FROM Kunde WHERE Nummer = ?'
            cursor.execute(query, (phone,))
        
        result = cursor.fetchone()

        if result:
            return result[0]
        else:
            return None



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

def check_user_story_g():
    # Get user input for train route
    train_route = input("Enter the train route name: ")

    # Query available seats
    cursor.execute("""
    SELECT Vogn.VognID, Sete.SeteID
    FROM Sete
    JOIN Vogn ON Sete.VognID = Vogn.VognID
    WHERE Vogn.TogRuteNavn = ? AND Sete.Tilgjengelig = 1
    """, (train_route,))
    available_seats = cursor.fetchall()

    # Query available beds
    cursor.execute("""
    SELECT Seng.VognID, Seng.KupeID, Seng.SengID
    FROM Seng
    JOIN Kupe ON Seng.KupeID = Kupe.KupeID AND Seng.VognID = Kupe.VognID
    JOIN Vogn ON Seng.VognID = Vogn.VognID
    WHERE Vogn.TogRuteNavn = ? AND Seng.Tilgjengelig = 1
    """, (train_route,))
    available_beds = cursor.fetchall()

    # Print available seats and beds
    print("Available seats:")
    for seat in available_seats:
        print(f"VognID: {seat[0]}, SeteID: {seat[1]}")

    print("\nAvailable beds:")
    for bed in available_beds:
        print(f"VognID: {bed[0]}, KupeID: {bed[1]}, SengID: {bed[2]}")

    # Get user input for selected ticket (seat or bed)
    ticket_type = input("Enter 'seat' to purchase a seat or 'bed' to purchase a bed: ")
    if ticket_type.lower() == 'seat':
        vogn_id = int(input("Enter the VognID for the seat you want to purchase: "))
        sete_id = int(input("Enter the SeteID for the seat you want to purchase: "))

        cursor.execute("UPDATE Sete SET Tilgjengelig = 0 WHERE SeteID = ? AND VognID = ?", (sete_id, vogn_id))
        con.commit()
        print("Seat purchased successfully!")

    elif ticket_type.lower() == 'bed':
        vogn_id = int(input("Enter the VognID for the bed you want to purchase: "))
        kupe_id = int(input("Enter the KupeID for the bed you want to purchase: "))
        seng_id = int(input("Enter the SengID for the bed you want to purchase: "))

        cursor.execute("UPDATE Seng SET Tilgjengelig = 0 WHERE SengID = ? AND KupeID = ? AND VognID = ?", (seng_id, kupe_id, vogn_id))
        con.commit()
        print("Bed purchased successfully!")
    else:
        print("Invalid input. Please try again.")


def check_user_story_h():
    user_input = input("Enter your name or phone number: ")

    if user_input.isdigit():
        user_id = get_user_id_by_name_or_phone(phone=user_input)
    else:
        user_id = get_user_id_by_name_or_phone(name=user_input)

    if user_id:
        with sqlite3.connect("TogDB.db") as conn:
            cursor = conn.cursor()

            query = '''
            SELECT KundeOrdre.OrdreID, KundeOrdre.Dato, KundeOrdre.TogruteNavn, KundeOrdre.AntallBilletter, Billett.BillettID, Billett.VognID, Billett.SeteID, Billett.KupeID, Billett.SengID
            FROM KundeOrdre
            JOIN Billett ON KundeOrdre.BillettID = Billett.BillettID
            WHERE KundeOrdre.KundeID = ?
            '''

            cursor.execute(query, (user_id,))
            result = cursor.fetchall()

        print(f"Tickets purchased by user {user_id}:")
        for row in result:
            print(f"Order ID: {row[0]}, Date: {row[1]}, Route: {row[2]}, Number of tickets: {row[3]}, Ticket ID: {row[4]}, Vogn ID: {row[5]}, Seat ID: {row[6]}, Kupe ID: {row[7]}, Bed ID: {row[8]}")
    else:
        print("No user found with the given name or phone number.")
