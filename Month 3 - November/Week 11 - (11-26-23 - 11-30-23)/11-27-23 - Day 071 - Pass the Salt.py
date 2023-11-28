import os
import random
from replit import db

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def new_user():
  clear_screen()
  username = input("Enter a username: ")
  password = input("Enter a password: ")

  if username in db:
    print("ERROR: User already exists")
    return

  salt = random.randint(1, 9999)
  formatted_salt = f"{salt:04d}"
  new_password = f"{password}{formatted_salt}"
  new_password = hash(new_password)
  db[username] = {"password": new_password, "salt": formatted_salt}
  print("Account created.")

def login():
  clear_screen()
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  keys = db.keys()
  if username not in keys:
    print("ERROR: User does not exist")
    return

  salt = db[username]["salt"]
  new_password = f"{password}{salt}"
  new_password = hash(new_password)

  if db[username]["password"] == new_password:
    print("Logged in")
  else:
    print("Username or password incorrect")

while True:
  menu = input("1: Create account\n2: Login\n> ")
  if menu == "1":
    new_user()
  elif menu == "2":
    login()
  else:
    print("Please select a valid option.")