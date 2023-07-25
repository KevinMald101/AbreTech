import sqlite3
import time
con = sqlite3.connect("SQlite/dataBase/opportunities.db")
cur = con.cursor() # Cursor used
# Questions
def questions():
  reward = int(input("What would be the minimum reward: "))
  '''
  print(
  """
  Do you have a specific major in mind?
  Here's the list of majors
  Or if you want scholarships with no 'major' specific, then type 'none'.""")
  time.sleep(5)
  
  major = input(
  """
  art, history, computer science
  mathematics, criminal Justice, tv media
  culinary, engineering, electrical
  business, graphic design, psychology
  health tech, music, chemistry
  carpentry, physics, marketing
  education, marine biology, Web Development\n""").lower()
  '''
  gpa = float(input("Type your gpa or type '0' if you want scholarships with no gpa requirements\n"))
  #essay = input("Want scholarships with an essay requirement (y/n): ").lower()
  #if major == 'none':
  #  major = 'NULL'
  '''
  if essay == 'y':
    essay = 'yes'
  elif essay == 'n':
    essay = 'no'
  '''
  return reward, gpa

def querying():
  con = sqlite3.connect("SQlite/dataBase/opportunities.db")
  cur = con.cursor() # Cursor used
  reward, gpa = questions()
  try:
    #cur.execute("SELECT * FROM scholarships WHERE reward >= ? AND major = ? AND gpa >= ? AND essay = ?", (reward, major, gpa, essay))
    cur.execute('SELECT * FROM scholarships WHERE reward >= ? AND gpa <= ?', (reward, gpa))
    results = cur.fetchall()
    print("(name, reward, start, deadline, major, gpa, location, essay)")
    for row in results:
      print(row)
  except sqlite3.Error as problem:
    print("Error executing the query:", problem)
querying()
con.close()
'''
⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜
⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜
⬛⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬛⬜⬛
⬛⬜⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬛
⬛⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜⬜⬛⬜⬛⬛⬜⬜⬛
⬜⬛⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬛⬜
⬜⬜⬛⬛⬜⬜⬛⬜⬜⬜⬜⬜⬜⬛⬜⬜⬛⬛⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬛⬜⬜⬛⬛⬛⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜⬜
⬜⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜⬜
⬜⬜⬛⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬛⬜⬜
⬜⬜⬛⬜⬜⬛⬜⬛⬛⬛⬛⬛⬛⬜⬛⬜⬜⬛⬜⬜
⬜⬜⬜⬛⬛⬛⬜⬛⬜⬛⬛⬜⬛⬜⬛⬛⬛⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬛⬛⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬛⬛⬛⬛⬜⬜⬛⬛⬛⬛⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜
'''