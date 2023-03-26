import sqlite3
from core import *
from initDB import *
from dummydata import *

# Creates a connection to out database
con = sqlite3.connect("TogDB.db")

# Creates a connecting object to our database
cursor = con.cursor()

# Populate the database with necessary data
populateDB()

# Used to test user story a)
check_user_story_a()
print("\n")

# Used to test user story b)
check_user_story_b()
print("\n")

# Used to test user story c)
#check_user_story_c()
print("\n")
"""
# Used to test user story d)
check_user_story_d()
print("\n")

# Used to test user story e)
check_user_story_e()
print("\n")

# Used to test user story g)
check_user_story_g()
print("\n")

# Used to test user story h)
check_user_story_h()
print("\n")
"""

#Save changes to database
con.commit()
# Close connection to database
con.close()
