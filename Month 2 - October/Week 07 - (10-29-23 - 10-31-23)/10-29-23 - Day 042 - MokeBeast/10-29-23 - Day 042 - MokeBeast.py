import os

print("Mokèdex")

mokèmon = {"name": None, "type": None, "move": None, "hp": None, "mp": None}

for name in mokèmon.keys():
  if name == "name":
    name_input = input(f"Please enter the name of your Mokèmon: ")
    mokèmon[name] = name_input
  elif name == "type":
    type_input = input("Please enter the type of your Mokèmon (Earth, Fire, Air, Water, Spirit): ").lower()
    if type_input in ["earth", "fire", "air", "water", "spirit"]:
        mokèmon[name] = type_input
    else:
        print("Invalid type. Please enter one of the valid types: Earth, Fire, Air, Water, Spirit.")
  elif name == "move":
    move_input = input(f"Please enter the special move of your Mokèmon: ")
    mokèmon[name] = move_input
  elif name == "hp":
    hp_input = input("Please enter the HP of your Mokèmon: ")
    if hp_input.isnumeric():
      mokèmon[name] = int(hp_input)
    else:
      print("Invalid input. HP must be a numeric value.")
  elif name == "mp":
    mp_input = input("Please enter the MP of your Mokèmon: ")
    if mp_input.isnumeric():
      mokèmon[name] = int(mp_input)
    else:
      print("Invalid input. MP must be a numeric value.")

os.system("clear")

for name, value in mokèmon.items():
  if name.lower() == "type":
    if value.lower() == "fire":
      print('\033[31m')
    elif value.lower() == "water":
      print('\033[34m')
    elif value.lower() == "air":
      print('\033[37m')
    elif value.lower() == "earth":
      print('\033[32m')
    elif value.lower() == "spirit":
      print('\033[33m')

for name, value in mokèmon.items():
  if name.lower() == "hp":
    print(f"{name.upper()}: {value}")
  elif name.lower() == "mp":
    print(f"{name.upper()}: {value}")
  else:
    print(f"{name.title()}: {value.title()}")