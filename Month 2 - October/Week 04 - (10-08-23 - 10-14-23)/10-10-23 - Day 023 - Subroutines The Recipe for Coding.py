def login():
    print("Login")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return username, password
while True:
  username, password = login()
  if username == "admin" and password == "admin":
    print("Welcome admin")
    break
  else:
    print("Invalid username or password")