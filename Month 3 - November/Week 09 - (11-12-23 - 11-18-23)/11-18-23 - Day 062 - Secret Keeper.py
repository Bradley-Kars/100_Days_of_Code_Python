from replit import db
import datetime, os, time

def addEntry():
  os.system("clear")
  timestamp = datetime.datetime.now()
  formatted_timestamp = timestamp.strftime("%Y-%m-%d %H:%M:%S")
  print(f"Diary entry for {formatted_timestamp}")
  entry = input("> ")
  db[formatted_timestamp] = entry

def viewEntry():
  keys = sorted(db.keys())
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"{key}")
    print("Entry:")
    if key == "password":
      print("*****")
    else:
      print(db[key])
    print()
    opt = input("Next or exit? > ")
    if opt.lower()[0] == "e":
      break

stored_password = db.get("password")

if not stored_password:
  new_password = input("Set a new password: ")
  db["password"] = new_password
  print("Password set successfully!")
  exit()

password = input("Password: ")
if password != stored_password:
  print("Incorrect")
  exit()

while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()