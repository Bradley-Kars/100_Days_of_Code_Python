import re
from datetime import datetime

name = input("What is your name?: ")
while True:
    dob = input("What is your DoB? (MM-DD-YYYY): ")
    try:
        dob_date = datetime.strptime(dob, "%m-%d-%Y")
        break
    except ValueError:
        print("Please enter a valid date in the format MM-DD-YYYY.")
while True:
    tel = input("What is your telephone number?: ")
    if tel.isdigit():
        break  # Exit the loop if it contains only numbers
    else:
        print("Please enter a valid telephone number (numbers only).")
while True:
    email = input("What is your email address?: ")
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):
        break  # Exit the loop if it's a valid email
    else:
        print("Please enter a valid email address.")
address = input("What is your address?: ")

dob_date = datetime.strptime(dob, "%m-%d-%Y")
current_date = datetime.now()
age = current_date.year - dob_date.year - ((current_date.month, current_date.day) < (dob_date.month, dob_date.day))

contactCard= {"name": name, "age": age, "number": tel, "email": email, "address": address}
print()
print(f"""Name: {contactCard["name"]}""")
print(f"""Age: {contactCard["age"]}""")
print(f"""Tel: {contactCard["number"]}""")
print(f"""Email: {contactCard["email"]}""")
print(f"""Address: {contactCard["address"]}""")