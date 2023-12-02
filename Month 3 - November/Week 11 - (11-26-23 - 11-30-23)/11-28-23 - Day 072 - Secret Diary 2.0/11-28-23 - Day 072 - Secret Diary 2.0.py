from replit import db
import datetime, os, time, random

def addEntry():
  time.sleep(1)
  os.system("clear")
  timestamp = datetime.datetime.now()
  print(f"Diary entry for {timestamp}")
  print()
  entry = input("> ")
  db[timestamp] = entry

def viewEntry():
  keys = db.prefix("2")
  for key in keys:
    time.sleep(1)
    os.system("clear")
    print(f"{key}\n{db[key]}")
    print()
    opt = input("Next or exit? > ")
    if opt.lower()[0] == "e":
      break

keys = db.keys()

if len(keys) < 1:
  print("Create your account")
  username = input("Username: ")
  password = input("Password: ")
  salt = random.randint(1, 9999)
  formatted_salt = f"{salt:04d}"
  new_password = f"{password}{formatted_salt}"
  new_password = hash(new_password)
  db[username] = {"password": new_password, "salt": salt}
else:
  print("Log in")
  username = input("Username: ")
  password = input("Password: ")
  if username not in keys or db[username]["password"] != hash(f"{password}{db[username]['salt']}"):
      print("Username or password incorrect")
      exit()

while True:
  os.system("clear")
  menu = input("1: Add\n2: View\n> ")
  if menu == "1":
    addEntry()
  else:
    viewEntry()