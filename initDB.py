import sqlite3


def initDB():
    """
    This function initializes the DB with necessary tables.
    """

    # Creates a connection to out DB
    con = sqlite3.connect("TogDB.db")

    # Reads SQL script from file
    with open('Jernbane.sql', 'r') as f:
        sql_script = f.read()

    # Execute the script that initializes the DB
    con.executescript(sql_script)

    # Commit the changes aka "Save"
    con.commit()

    # Good practice to close the DB after access
    con.close()
