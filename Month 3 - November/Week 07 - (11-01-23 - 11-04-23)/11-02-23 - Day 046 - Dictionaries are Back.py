import os

print("Mokèdex V2")

mokedex = {}

while True:
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
        print("Invalid input. MP must be a numeric value")

  os.system("clear")

  mokedex[mokèmon["name"]] = {
      "type": mokèmon["type"],
      "move": mokèmon["move"],
      "hp": mokèmon["hp"],
      "mp": mokèmon["mp"]
  }

  print("Mokèmon added to Mokèdex:")
  for name, value in mokèmon.items():
    if name.lower() == "hp" or name.lower() == "mp":
      print(f"{name.upper()}: {value}")
    else:
      print(f"{name.title()}: {value.title()}")

  print()

  print("Mokèdex:")
  for name, data in mokedex.items():
    print(f"Name: {name}")
    for attribute, value in data.items():
      print(f"{attribute.upper()}: {value}")
    print()