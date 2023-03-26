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
    """, (station_name, day_of_week))

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


def get_user_by_phone_number(phone_number):
    cursor.execute("SELECT * FROM Kunde WHERE Nummer=?", (phone_number,))
    user = cursor.fetchone()
    return user


def check_user_story_a():
    """This function is used to test user story a)"""

    print("USER STORY A")
    cursor.execute("SELECT * FROM Banestrekning")
    banestrekningrows = cursor.fetchall()
    for banestrekning in banestrekningrows:
        cursor.execute("SELECT SUM(LengdeIKm) FROM Delstrekning")
        totalLength = cursor.fetchall()
        # Underneath line includes just a lot of formatting in order to look "pretty" in terminal output
        print(f'"{banestrekning[1]}" has fuel fource "{banestrekning[2]}",\nwith total length {str(totalLength[0]).replace("(", "").replace(")", "").replace(",", "")}km,\nand includes the following stations:')
        cursor.execute("SELECT * FROM Stasjon")
        stasjonsrows = cursor.fetchall()
        for stasjon in stasjonsrows:
            print(f"{stasjon[0]} | {stasjon[1]} Moh")


def check_user_story_b():
    """This function is used to test user story b)"""

    print("USER STORY B")
    cursor.execute("SELECT * FROM Togrute")
    togruterows = cursor.fetchall()
    print("3 Routes Are Available:")
    for i in range(0, len(togruterows), 2):
        print("\n")
        cursor.execute(
            "SELECT * FROM RUTESTOPP WHERE Rutestopp.TogruteNavn = ?", (togruterows[i][0],))
        rutestopprows = reversed(cursor.fetchall())
        print(str(togruterows[i][0]) +
              f" departs on the {str(togruterows[i][1])} and has the following schedule: ")
        for rutestopp in rutestopprows:
            print(rutestopp[1] + " | " + rutestopp[2])


def check_user_story_c():
    """This function is used to test user story c)"""

    print("USER STORY C")
    station_name = get_station_name()
    # You can use Norwegian days like "Mandag" if your data is in Norwegian
    day_of_week = get_weekday()
    train_routes = get_train_routes_by_station_and_day(
        station_name, day_of_week)
    print("\n")
    print(f"Train routes passing through {station_name} on {day_of_week}: \n")
    if len(train_routes) != 0:
        for train_route in train_routes:
            print(train_route[0])
    else:
        print("No Routes Available")


def check_user_story_d():
    """This function is used to test user story d)"""

    start_station = get_station_name()
    end_station = get_station_name()
    date = get_date()
    time = get_time()
    train_routes = get_train_routes(start_station, end_station, date, time)
    print(
        f"Train routes from {start_station} to {end_station} on {date} at {time}:")
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


current_user = None


def check_user_story_g():
    global current_user

    while not current_user:
        choice = input(
            "Enter 'login' to log in, 'register' to register, or 'guest' to continue as a guest: ").lower()
        if choice == 'login':
            phone_number = get_phone_number()
            current_user = get_user_by_phone_number(phone_number)
            if not current_user:
                print("User not found. Please try again.")
            else:
                print("Logged in successfully!")
        elif choice == 'register':
            name = get_name()
            e_mail = get_e_mail()
            phone_number = get_phone_number()
            register_user(name, e_mail, phone_number)
        else:
            print("Invalid choice. Please try again.")

    # User is logged in or provided their name and phone number, continue with the ticket purchase process
    # ...

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
    ticket_type = input(
        "Enter 'seat' to purchase a seat or 'bed' to purchase a bed: ")
    if ticket_type.lower() == 'seat':
        vogn_id = int(
            input("Enter the VognID for the seat you want to purchase: "))
        sete_id = int(
            input("Enter the SeteID for the seat you want to purchase: "))

        cursor.execute(
            "UPDATE Sete SET Tilgjengelig = 0 WHERE SeteID = ? AND VognID = ?", (sete_id, vogn_id))
        con.commit()
        print("Seat purchased successfully!")

    elif ticket_type.lower() == 'bed':
        vogn_id = int(
            input("Enter the VognID for the bed you want to purchase: "))
        kupe_id = int(
            input("Enter the KupeID for the bed you want to purchase: "))
        seng_id = int(
            input("Enter the SengID for the bed you want to purchase: "))

        cursor.execute(
            "UPDATE Seng SET Tilgjengelig = 0 WHERE SengID = ? AND KupeID = ? AND VognID = ?", (seng_id, kupe_id, vogn_id))
        cursor.execute("INSERT INTO KundeOrdre (Ordre.ID, KundeID, BillettID, Dato, TogruteNavn, AntallBilletter) VALUES (1, ?, 1, ?, ?, ?)",
                       (current_user[0], '2023-04-03', train_route, 1))
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
