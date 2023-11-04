import os, time, random

trumps = {}
trumps["Goku"] = {"Intelligence": 76, "Speed": 334821428, "Strength": 464}
trumps["Saitama"] = {"Intelligence": 90, "Speed": 573249600, "Strength": 1252224160000000000000000}
trumps["Mob"] = {"Intelligence": 130, "Speed": 500, "Strength": 50}
trumps["Ichigo"] = {"Intelligence": 100, "Speed": 6564, "Strength": 50}
trumps["Luffy"] = {"Intelligence": 90, "Speed": 997450, "Strength": 280}

while True:
  print("ANIME TRUMPS\n")
  print("Characters\n")
  for key in trumps:
    print(key)
  user = input("\nPick your character: ")
  while user not in trumps:
      print("Invalid character choice. Please pick a character from the list.")
      user = input("\nPick your character: ")
  comp = user
  while comp == user:
    comp = random.choice(list(trumps.keys()))
  print("\nComputer has picked", comp)

  print()

  answer = input("Choose your stat: Intelligence, Speed, or Strength: ").title()
  while answer not in ["Intelligence", "Speed", "Strength"]:
      print("Invalid choice. Please pick one of the specified options.")
      answer = input("Choose your stat: Intelligence, Speed, or Strength: ").title()

  print(f"{user}: {trumps[user][answer]} {'tons' if answer == 'Strength' else 'MPH' if answer == 'Speed' else 'IQ'}")
  print(f"{comp}: {trumps[comp][answer]} {'tons' if answer == 'Strength' else 'MPH' if answer == 'Speed' else 'IQ'}")

  if trumps[user][answer] > trumps[comp][answer]:
    print(f"\n{user} wins")
  elif trumps[user][answer] < trumps[comp][answer]:
    print(f"\n{comp} wins")
  else:
    print("\nDraw")

  time.sleep(5)
  os.system("clear")