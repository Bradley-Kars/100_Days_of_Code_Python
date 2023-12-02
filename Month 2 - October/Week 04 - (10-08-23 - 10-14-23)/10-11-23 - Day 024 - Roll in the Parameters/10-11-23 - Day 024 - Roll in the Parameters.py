import random

def dice(maxSides):
  while True:
    roll = random.randint(1, maxSides)
    print("\nYou rolled", roll)
    repeat = input("\nWould you like to roll again? (yes/no): ")
    if repeat.lower() != "yes":
      break

print("Ultimate dice!")

maxSides= int(input("\nHow many sides does this dice have?: "))
dice(maxSides)