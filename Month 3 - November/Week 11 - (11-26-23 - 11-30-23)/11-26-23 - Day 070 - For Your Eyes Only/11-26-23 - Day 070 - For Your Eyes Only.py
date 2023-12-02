import os

def authenticate(username, password):
  user_password = os.environ.get('password')
  admin_password = os.environ.get('admin_password')

  if username == "user" and password == user_password:
    return "Welcome user!"
  elif username == "admin" and password == admin_password:
    return "Welcome admin!"
  else:
    return "Incorrect login!"

username = input("Username: ")
user_pass = input("Password: ")

print(authenticate(username, user_pass))