from replit import db
import datetime
import os
import time

def add_cheep():
  cheep = input("Cheep: \n")
  timestamp = datetime.datetime.now()
  key = f"mes{timestamp}"
  db[key] = cheep
  time.sleep(1)
  os.system("clear")

def view_cheeps():
  matches = db.prefix("mes")
  matches = matches[::-1]
  counter = 0

  for i in matches:
    print(db[i], end="\n\n")
    time.sleep(0.3)
    counter += 1

    if counter % 10 == 0:
      carry_on = input("Would you like to see the next 10 cheeps?: ")
      if carry_on.lower() == "no":
          break

  time.sleep(1)
  os.system("clear")

while True:
  print("cheeper")
  menu = input("1: Add Cheeep\n2: View Cheeps\n> ")

  if menu == "1":
    add_cheep()
  elif menu == "2":
    view_cheeps()
  else:
    print("Invalid option. Please choose 1 or 2.")