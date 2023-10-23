nameList = []

def printList():
  print()
  for index, item in enumerate(nameList, start=1):
      print(f'{index}: {item}')
  print()

while True:
  firstName = input("What is your first name?: ").title().strip()
  lastName = input("What is your last name?: ").title().strip()
  fullName = f"{firstName} {lastName}"
  if fullName not in nameList:
    nameList.append(fullName)
  else:
    print("Error: Name already in list")
  printList()