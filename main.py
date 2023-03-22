import sqlite3
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

# Save changes to database
con.commit()
# Close connection to database
con.close()
