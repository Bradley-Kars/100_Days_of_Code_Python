import random

def rollDice(sides):
  roll = random.randint(1,sides)
  return roll

def playerCreator():
  playerName = input("\nWhat is your Characters name?: ") 
  playerHP = rollDice(6) * rollDice(8)
  print("\n"+playerName, "has", playerHP, "health.")

print("Character Creator!")

while True:
  playerCreator()
  repeat = input("\nWould you like to make another character?: ")
  if repeat.lower() != "yes":
    break