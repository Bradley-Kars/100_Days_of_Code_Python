import os, time, sys

to_do = []

try:
    with open("to.do", "r") as f:
        data = f.read()
        if data:
            to_do = eval(data)
except FileNotFoundError:
    print("File 'to.do' does not exist. Creating an empty list.")
    to_do = []

def printList():
  print()
  max_width = len(str(len(to_do)))
  for index, item in enumerate(to_do, start=1):
      print(f'{index:>{max_width}}: {item}')
  print()

while True:
  task = input("\nWould you like to view your to do list (view), add a task (add), edit (edit), or remove an existing task (remove)?: ")
  if task.lower() == "view":
    os.system("clear")
    printList()
  elif task.lower() == "add":
    item = input("\nWhat would you like to add to your list?: ")
    if item not in to_do:
      to_do.append(item)
      os.system("clear")
  elif task.lower() == "edit":
    printList()
    print()
    try:
      editNumber = int(input("What to do number would you like to edit?: "))
      if 1 <= editNumber <= len(to_do):
          editToDo = input(f"What would you like task number {editNumber} to say?: ")
          to_do[editNumber - 1] = editToDo
      else:
          print("Invalid task number. Please enter a valid task number.")
    except ValueError:
      print("Invalid input. Please enter a number for the task number.")
  elif task.lower() == "remove":
    printList()
    item = input("\nWhat would you like to remove from your list?: ")
    if item in to_do:
      check = input(f"Are you sure you'd like to remove {item} from your list?: ")
      if check == "yes":
        to_do.remove(item)
        os.system("clear")
        print(f"{item}, has been removed from your list.")
    else:
      print("\n" + item, "was not in your list.")
      time.sleep(1)
      os.system("clear")
  elif task.lower() == "exit":
    os.system("clear")
    sys.exit()
  else:
    print("\nThat was not a proper input.")
  f = open("to.do", "w") 
  f.write(str(to_do)) 
  f.close()