import os
import time
import re

todo = []

def validate_date_time(input_str):
    date_pattern = r'^\d{2}/\d{2}/\d{4}$'
    time_pattern = r'^\d{2}:\d{2} (AM|PM)$'
    if re.match(date_pattern, input_str):
        return True
    elif re.match(time_pattern, input_str):
        return True
    else:
        return False

def get_priority():
  while True:
      priority = input("What is the priority of this task (low, medium, high)?: ").strip().capitalize()
      if priority in ["Low", "Medium", "High"]:
          return priority
      else:
          print("Invalid priority. Please enter 'low,' 'medium,' or 'high'.")

def add():
    os.system("clear")
    task = input("What do you need to do?: ")
    due_date = input("When is this task due (mm/dd/yyyy or xx:xx AM/PM)?: ")
    if not validate_date_time(due_date):
        print("Invalid date or time format. Please enter a valid date (mm/dd/yyyy) or time (xx:xx AM/PM).")
        time.sleep(1.5)
        return
    priority = get_priority()
    row = [task, due_date, priority]
    todo.append(row)
    print("Task has been added!")

def view():
  os.system("clear")
  options = input("1: All\n2: By Priority\n> ")
  if options == "1":
    column_widths = [0] * 3  # Initialize column widths for task, due_date, and priority
    for row in todo:
      for i, item in enumerate(row):
        column_widths[i] = max(column_widths[i], len(str(item)))
    for row in todo:
      for i, item in enumerate(row):
        print(f"{item:{column_widths[i]}}", end=" | ")
      print()
    print()
  else:
    priority = input("What priority?: ").capitalize()
    column_widths = [0] * 3
    filtered_rows = [row for row in todo if priority in row]
    for row in filtered_rows:
      for i, item in enumerate(row):
        column_widths[i] = max(column_widths[i], len(str(item)))
    for row in filtered_rows:
      for i, item in enumerate(row):
        print(f"{item:{column_widths[i]}}", end=" | ")
      print()
    print()
  time.sleep(1)


def edit():
  os.system("clear")
  find = input("Name of task to edit: ")
  found = False
  for row in todo:
      if find in row:
          found = True
  if not found:
      print("Task could not be found!")
      return
  for row in todo:
      if find in row:
          todo.remove(row)
  task = input("What do you need to do?: ")
  due_date = input("When is this task due (mm/dd/yyyy or xx:xx AM/PM)?: ")
  if not validate_date_time(due_date):
      print("Invalid date or time format. Please enter a valid date (mm/dd/yyyy) or time (xx:xx AM/PM).")
      time.sleep(1.5)
      return
  priority = get_priority()
  row = [task, due_date, priority]
  todo.append(row)
  print("Added")

def remove():
  os.system("clear")
  find = input("What task would you like to remove: ")
  for row in todo:
    if find in row:
      todo.remove(row)

while True:
  menu = input("1: Add\n2: View\n3: Edit\n4: Remove\n> ")
  if menu == "1":
    add()
  elif menu == "2":
    view()
  elif menu == "3":
    edit()
  elif menu == "4":
    remove()
  else:
    print("Please select one of the provided options.")
  time.sleep(1.5)
  os.system("clear")