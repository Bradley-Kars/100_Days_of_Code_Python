import os, random

print("Idea Storage")
print()

while True:
  while True:
    try:
      choice = int(input("What would you like to do?\n1. Add an idea\n2. Load a random idea\n3. Exit\n"))
      if choice in [1, 2, 3]:
        break
      else:
        print("Please enter a valid choice (1, 2, or 3).")
    except ValueError:
      print("Please enter a valid integer (1, 2, or 3).")
  if choice == 1:
    os.system("clear")
    idea = input("Whats idea would you like to add?:\n")
    f = open("my.idea", "a+")
    f.write(f"{idea}\n")
    f.close()
    os.system("clear")
  elif choice == 2:
    os.system("clear")
    with open("my.idea", "r") as f:
      lines = f.readlines()
      if lines:
        random_index = random.randint(0, len(lines) - 1)
        random_idea = lines[random_index].strip()
        print("Random Idea:", random_idea)
        input("Press Enter to continue...")
        os.system("clear")
      else:
        print("No ideas found.")
        input("Press Enter to continue...")
        os.system("clear")
  elif choice == 3:
    os.system("clear")
    break
  else:
    print("invalid input, please try again.")