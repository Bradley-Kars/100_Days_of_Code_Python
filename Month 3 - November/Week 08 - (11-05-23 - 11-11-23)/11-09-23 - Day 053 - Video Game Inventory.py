import os
import time
import json

game_inventory = []

def load_inventory():
  try:
    with open("game.inv", "r") as file:
      game_inventory.extend(json.load(file))
  except FileNotFoundError:
    print("ERROR: No existing inventory, using a blank list")

def view_inventory():
  headers = ["Item", "Quantity"]
  print(f"{headers[0]:^10}{headers[1]:^10}")
  for row in game_inventory:
    print(f"{row[0]:^10}{row[1]:^10}")
  input("Press Enter to continue...")

def remove_item():
  time.sleep(1)
  os.system("clear")
  view_inventory()
  print()
  name = input("Name of the item to remove: ").capitalize()
  
  for item in game_inventory:
    if item[0] == name:
      while True:
        try:
          qty_to_remove = int(input(f"Quantity to remove (current quantity: {item[1]}): "))
          break
        except ValueError:
          print("Error: Quantity must be a whole number")

      if qty_to_remove >= item[1]:
        game_inventory.remove(item)
      else:
        item[1] -= qty_to_remove
      return
  
  print(f"Item '{name}' not found in the inventory.")

def add_item():
  time.sleep(1)
  os.system("clear")
  name = input("Name: ").capitalize()

  for _ in range(3):  # Allow three attempts for valid input
    try:
      qty = int(input("Quantity: "))
      break
    except ValueError:
      print("Error: Quantity must be a whole number")
  else:
    print("Too many invalid attempts. Exiting.")
    return

  for item in game_inventory:
    if item[0] == name:
      item[1] += qty
      return

  row = [name, qty]
  game_inventory.append(row)

def main():
  load_inventory()

  while True:
    time.sleep(1)
    os.system("clear")
    print("Inventory")
    print()
    menu = input("1: Add Item\n2: Remove Item\n3: View Inventory\n> ")

    if menu == "1":
      add_item()
    elif menu == "2":
      remove_item()
    elif menu == "3":
      view_inventory()

    with open("game.inv", "w") as file:
      json.dump(game_inventory, file)

if __name__ == "__main__":
    main()