import os, time
listOfEmail = []

bold_red = "\033[1;31m"
reset = "\033[0m"

def prettyPrint():
  os.system("clear") 
  print("listofEmail") 
  print()
  counter = 1 
  for email in listOfEmail: 
    width = len(str(len(listOfEmail)))
    print(f'{counter:{width}}: {email}')
    counter += 1 
  time.sleep(2)

def get_spam_count():
  while True:
      try:
          spamCount = int(input("How many emails would you like to send?: "))
          if spamCount <= 0:
              print("Please enter a positive number.")
          else:
              spamCount = min(spamCount, len(listOfEmail))
              return spamCount
      except ValueError:
          print("Invalid input. Please enter a valid integer.")

def spamming(spamCount):
  print("Begining spam:")
  print()
  for email in listOfEmail[:spamCount]:
    print(f"dear {email},\nWe've been trying to reach you concerning your vehicle's extended warranty. You should've received a notice in by e-mail about your car's extended warranty eligibility. Since we've not gotten a response, we're giving you a {bold_red}final{reset} courtesy message before we {bold_red}close{reset} out your file. Reply 'REM0VE' to be removed and placed on our do-not-mail list. To message to someone about possibly extending or reinstating your vehicle's warranty, reply 'REMOVE' to speak with a warranty specialist.\n\nYours truly,\nElongated Muskrat")
    print()
    time.sleep(2)
    os.system("clear")
    

while True:
  print("SPAMMER Inc.")
  menu = input("1. Add email\n2: Remove email\n3. Show emails\n4. Get SPAMMING\n> ")
  if menu == "1":
    email = input("Email > ")
    listOfEmail.append(email)
  elif menu =="2":
    email = input ("Email > ")
    if email in listOfEmail:
      listOfEmail.remove(email)
  elif menu == "3":
    prettyPrint()
  elif menu == "4":
    spamCount = get_spam_count()
    spamming(spamCount)
  else:
    print("that was not a valid selection, please try again.")
  time.sleep(1)
  os.system("clear")