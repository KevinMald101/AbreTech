import sqlite3
import csv
con = sqlite3.connect("SQlite/dataBase/opportunities.db")
cur = con.cursor() # Cursor used
cur.execute("DROP TABLE scholarships")
cur.execute("CREATE TABLE scholarships (name text, reward text, start text, deadline text, major text, gpa text, location text, essay text)")

# Sql code with placement variables at the end
sql = "INSERT INTO `scholarships` (`name`, `reward`, `start`, `deadline`, `major`, `gpa`, `location`, `essay`) VALUES (?,?,?,?,?,?,?,?)"
# Try this code and if it doesn't work give an error on what went wrong
try:
  # Open the csv file and make it a variable called 'scholarships'
  with open('SQlite/fakeScholarships.csv', 'r',encoding='utf-8-sig') as scholarships:
    reader = csv.DictReader(scholarships)
    # For each row in the csv file
    for row in reader:
      #print(row)
      # I know what's going on but don't know how, Justin the goat!
      val = (row['name'], row['reward'], row['start'], row['deadline'], row['major'], row['gpa'], row['location'], row['essay'])
      # The values of val will be used as variables for the sql statement
      cur.execute(sql, val) 
      # Commit the stuff
      con.commit()
  print("Database updated!")
  con.close()
except sqlite3.Error as bruh:
  print("Error:", bruh)

# Old way to insert stuff to the database, i got lazy and wanted to make it somewhat automated using a csv file
#cur.execute("CREATE TABLE scholarships (name text, reward int, start month text, deadline text, major text, gpa real, location text, essay text)")
#cur.execute("INSERT INTO scholarships VALUES ('sharko scholarship', 250, 'january', 'february', 'art', NULL, 'ohio', 'yes (250 words')")
#cur.execute("INSERT INTO scholarships VALUES ('lotto scholarship', 1500, 'july', 'august', 'none', 3.4, 'massachusetts', 'none')")
#cur.execute("INSERT INTO scholarships VALUES ('single buck scholarship', 1, 'january', 'december', 'none', 2.0, 'georgia', 'yes (1 word)')")
#cur.execute("INSERT INTO scholarships VALUES ('jojos scholarship', 15000, 'may', 'september', 'history', 3.399, 'paris', 'yes (600 words)')")
'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣶⣶⣶⣶⣶⣶⣦⣄⡀⠀⠐⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣄⣼⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⣷⡦⠄⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⠀⠈⠀⠀⠀⠀
⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⡇⠀⠀⠀⠀
⠀⠀⠀⢰⣿⣿⣿⣯⣿⣿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⣿⣿⣿⡫⣁⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀
⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⡟⠃⣿⣿⣿⡟⠁⠀⠉⠛⠛⢻⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⡿⢿⣿⣯⡽⠿⠛⠉⠀⠀⠀⣬⠽⢷⣶⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀
⠀⠀⠀⣠⠋⢀⠙⡏⠁⣀⣾⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⡇⠘⣿⢉⡄⠱⡄⠀⠀⠀
⠀⠀⠀⢇⠀⠲⣹⣿⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⢸⡟⡡⠀⠠⠃⠀⠀⠀
⠀⠀⠀⠈⠱⢄⡈⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⠀⠀⠀⠀⠀⠀⢀⡎⠁⢀⠔⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠜⠉⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠒⡀⠀⠀⠀⠀⠐⠒⠀⠀⠀⠀⢀⠖⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢢⣤⡀⠀⠀⠀⣠⣤⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⢾⠿⣿⣿⣿⣿⣿⡿⣗⡆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠘⡞⠀⠈⠙⠛⠛⠉⠀⢻⠇⠈⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⣀⣴⡿⠀⠀⠰⣀⠀⠀⠀⠀⠀⢠⠇⠀⠀⢹⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀
'''