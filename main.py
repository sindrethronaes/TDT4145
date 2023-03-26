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

# Used to test user story b)
check_user_story_b()

# Used to test user story c)
check_user_story_c()

# Used to test user story d)
check_user_story_d()

# Used to test user story e)
check_user_story_e()

# Used to test user story g)
check_user_story_g()

# Used to test user story h)
check_user_story_h()

#Save changes to database
con.commit()
# Close connection to database
con.close()
