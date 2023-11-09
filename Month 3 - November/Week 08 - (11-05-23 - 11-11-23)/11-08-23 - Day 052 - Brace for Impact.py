import os
import time

pizza = []

def load_pizza_list():
  try:
    with open("pizza.txt", "r") as file:
      pizza_data = file.read()
      if pizza_data:
        pizza.extend(eval(pizza_data))
  except FileNotFoundError:
    print("ERROR: No existing pizza list, using a blank list")

def view_pizza():
  headers = ["Name", "Topping", "Size", "Quantity", "Total"]
  print(f"{headers[0]:^10}{headers[1]:^20}{headers[2]:^10}{headers[3]:^10}{headers[4]:^10}")
  for row in pizza:
      print(f"{row[0]:^10}{row[1]:^20}{row[2]:^10}{row[3]:^10}{row[4]:^10}")
  input("Press Enter to continue...")

def add_pizza():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ")
  toppings = input("Toppings: ")
  size = input("Size (s/m/l/xl): ").lower()

  while True:
    try:
      qty = int(input("Quantity: "))
      break
    except ValueError:
      print("Error: Quantity must be a whole number")

  cost = 0
  if size == "s":
    cost = 14.99
  elif size == "m":
    cost = 17.99
  elif size == "l":
    cost = 19.99
  else:
    cost = 22.49

  total = round(cost * qty, 2)
  row = [name, toppings, size, qty, total]
  pizza.append(row)

def main():
  load_pizza_list()

  while True:
    time.sleep(1)
    os.system("clear")
    print("Kars Pizza")
    print()
    menu = input("1: Add Pizza\n2: View Pizzas\n> ")

    if menu == "1":
      add_pizza()
    else:
      view_pizza()

    with open("pizza.txt", "w") as file:
      file.write(str(pizza))

if __name__ == "__main__":
  main()