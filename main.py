import sqlite3
from prettytable import PrettyTable
from inputFunctions import get_station_name, get_weekday
from core import *

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")

# Creates a connecting object to our database
cursor = con.cursor()

# Populate the database with necessary data
populateDB()

register_user()

# Used to test user story a)
check_user_story_a()

# Used to test user story b)
check_user_story_b()

station_name = get_station_name()
weekday = get_weekday()
# call function to get routes
routes = get_train_routes_for_station_on_weekday(station_name, weekday)

# print results
print(
    f"\nThe following routes stop at {station_name} on weekday number {weekday}:")
for route in routes:
    print(f"Route {route[0]} from {route[1]} to {route[2]}")

search_routes_menu()

# Run python main.py purchases <customer_id> in the terminal to see the upcoming purchases for a customer
def get_user_purchases(customer_id):
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

#Save changes to database
con.commit()
# Close connection to database
con.close()
