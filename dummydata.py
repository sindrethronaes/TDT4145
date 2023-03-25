import sqlite3
import uuid

def populateDB():
    con = sqlite3.connect("TogDB.db")
    cursor = con.cursor()

    # Reset the database
    cursor.execute("DELETE FROM Banestrekning")
    cursor.execute("DELETE FROM Stasjon")
    cursor.execute("DELETE FROM Delstrekning")
    cursor.execute("DELETE FROM Togrute")
    cursor.execute("DELETE FROM Sittevogn")
    cursor.execute("DELETE FROM Sovevogn")
    con.commit()

    # USER STORY a)
    cursor.execute(
        "INSERT INTO Banestrekning VALUES (1, 'Nordlandsbanen', 'Diesel')")

    # Insert information about Stasjoner
    cursor.execute("INSERT INTO Stasjon VALUES ('Trondheim', 5.1)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Steinskjer', 3.6)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Mosjøen', 6.8)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Mo i Rana', 3.5)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Fauske', 34.0)")
    cursor.execute("INSERT INTO Stasjon VALUES ('Bodø', 4.1)")

    # Insert information about Delstrekninger
    cursor.execute("INSERT INTO Delstrekning VALUES (1, 120, 1)")
    cursor.execute("INSERT INTO Delstrekning VALUES (2, 280, 0)")
    cursor.execute("INSERT INTO Delstrekning VALUES (3, 90, 0)")
    cursor.execute("INSERT INTO Delstrekning VALUES (4, 170, 0)")
    cursor.execute("INSERT INTO Delstrekning VALUES (5, 60, 0)")

    # USER STORY b)
    # Insert data for day train from Trondheim to Bodø into Togrute and Rutestopp
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn,Dato, DelstrekningID) VALUES ('dagtog fra trondheim til bodø', '2023-04-03', 1)")
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn,Dato, DelstrekningID) VALUES ('dagtog fra trondheim til bodø', '2023-04-04', 1)")
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
        "INSERT INTO Togrute(TogruteNavn, Dato, DelstrekningID) VALUES ('nattog fra Trondheim til Bodø', '2023-04-03', 1)")
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn, Dato, DelstrekningID) VALUES ('nattog fra Trondheim til Bodø', '2023-04-04', 1)")
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
        "INSERT INTO Togrute(TogruteNavn, Dato, DelstrekningID) VALUES ('morgentog fra Mo i Rana til Trondheim', '2023-04-03', 2)")
    cursor.execute(
        "INSERT INTO Togrute(TogruteNavn, Dato, DelstrekningID) VALUES ('morgentog fra Mo i Rana til Trondheim', '2023-04-04', 2)")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Mo i Rana', '08:11', 'NULL')")
    cursor.execute(
        "INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Mosjøen', '09:14', '09:14')")
    cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Steinkjer', '12:31', '12:31')")
    cursor.execute("INSERT INTO Rutestopp(TogruteNavn, StasjonNavn, Avgang, Ankomst) VALUES ('morgentog fra Mo i Rana til Trondheim', 'Trondheim S', 'NULL', '14:13')")

    # USER STORY f)
    # Inserts information regarding Operatører
    cursor.execute(
        "INSERT INTO Operatoer(OperatoerNavn, AntallVogntyper, Banestrekning) VALUES ('VY AS', 5,'Nordlandsbanen')")
    cursor.execute(
        "INSERT INTO Operatoer(OperatoerNavn, AntallVogntyper, Banestrekning) VALUES ('SJ Norge AS', 8,'Nordlandsbanen')")

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
        cursor.execute("INSERT INTO Vogn(Navn, VognType, OperatoerNavn) VALUES ('Sittevogn', 'SJ-sittevogn-1', 'SJ Norge AS' )")

    for i in range(11, 21):
        cursor.execute("INSERT INTO Vogn(Navn, VognType, OperatoerNavn) VALUES ('Sovevogn', 'SJ-sovevogn-1', 'SJ Norge AS' )")

    # Inserts information regarding seats (12 seats per car)
    for i in range(1, 11):
        for j in range(1, 13):
            cursor.execute(
                "INSERT INTO Sittevogn(VognID, AntallSeter, SeterPerRad) VALUES (?, ?, 4)",
                (str(uuid.uuid4()), j)
            )


    # Inserts information regarding beds (8 beds per car)
    for i in range(11, 21):
        for j in range(1, 9):
            cursor.execute(
                "INSERT INTO Sovevogn(VognID, AntallSenger, SengerPerKupe) VALUES (?, ?, 2)", (str(uuid.uuid4()), j))

    # Inserts information regarding Kupe
    for i in range(11, 21):
            for j in range(1, 5):
                cursor.execute(
                    "INSERT INTO Kupe(KupeID, VognID, Tilgjengelig) VALUES (?, ? , 1)", (j, i))

    # Inserts information regarding Seng (8 Beds in total per Kupe)
    for k in range(11, 21):
            for i in range(1, 5):
                for j in range(1, 3):
                    cursor.execute(
                        "INSERT INTO Seng(SengID, KupeID, VognID, Tilgjengelig) VALUES (?, ?, ?, 1)", (j, i, k))


    # Inserts information regarding Sete (12 Seats in total per Vogn)
    for i in range(1, 11):
        for j in range(1, 13):
            cursor.execute(
                "INSERT INTO Sete(SeteID, VognID, Tilgjengelig) VALUES (?, ?, 1)", (j, i))


    # Commit the changes aka "Saves" the DB-State
    con.commit()

    # Close the connection
    con.close()
