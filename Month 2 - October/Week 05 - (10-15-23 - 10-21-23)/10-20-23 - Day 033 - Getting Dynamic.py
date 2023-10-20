import os
import time

print("To do list manager!\n")

toDo = []

def printList():
  print()
  for item in toDo:
    print(item)
  print()

while True:
  task = input("\nWould you like to view your to do list (view), add a task (add), or remove an existing task (remove)?: ")
  if task.lower() == "view":
    os.system("clear")
    printList()
  elif task.lower() == "add":
    item = input("\nWhat would you like to add to your list?: ")
    toDo.append(item)
    os.system("clear")
  elif task.lower() == "remove":
    item = input("\nWhat would you like to remove from your list?: ")
    if item in toDo:
      toDo.remove(item)
      os.system("clear")
    else:
      print("\n" + item, "was not in your list.")
      time.sleep(1)
      os.system("clear")
  else:
    print("\nThat was not a proper input.")