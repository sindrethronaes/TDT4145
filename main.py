from core import *
from initDB import initDB

# Creates a connection to out database
initDB()

search_routes("Trondheim S", "Bodø", "2023-04-03", "07:49")

print("\n ok\n")
buy_ticket()

check_user_story_d()



# Used to test user story a)
check_user_story_a()

# Used to test user story b)
check_user_story_b()

# Used to test user story c)
check_user_story_c()

# Used to test user story d)

# Used to test user story e)
check_user_story_e()

# Used to test user story f)
check_user_story_f()

# Used to test user story g)

# Used to test user story h)
check_user_story_h()

#Save changes to database
con.commit()
# Close connection to database
con.close()
