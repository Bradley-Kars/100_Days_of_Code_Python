import os
import time

print("To do list manager!\n")

toDo = []

def printList():
  print()
  max_width = len(str(len(toDo)))
  for index, item in enumerate(toDo, start=1):
      print(f'{index:>{max_width}}: {item}')
  print()

while True:
  task = input("\nWould you like to view your to do list (view), add a task (add), edit (edit), or remove an existing task (remove)?: ")
  if task.lower() == "view":
    os.system("clear")
    printList()
  elif task.lower() == "add":
    item = input("\nWhat would you like to add to your list?: ")
    if item not in toDo:
      toDo.append(item)
      os.system("clear")
  elif task.lower() == "edit":
    printList()
    print()
    try:
      editNumber = int(input("What to do number would you like to edit?: "))
      if 1 <= editNumber <= len(toDo):
          editToDo = input(f"What would you like task number {editNumber} to say?: ")
          toDo[editNumber - 1] = editToDo
      else:
          print("Invalid task number. Please enter a valid task number.")
    except ValueError:
      print("Invalid input. Please enter a number for the task number.")
  elif task.lower() == "remove":
    item = input("\nWhat would you like to remove from your list?: ")
    if item in toDo:
      check = input(f"Are you sure you'd like to remove {item} from your list?: ")
      if check == "yes":
        toDo.remove(item)
        os.system("clear")
        print(f"{item}, has been removed from your list.")
    else:
      print("\n" + item, "was not in your list.")
      time.sleep(1)
      os.system("clear")
  else:
    print("\nThat was not a proper input.")