import random
import os

def rollDice(sides):
  roll = random.randint(1, sides)
  return roll

def playerCreator():
  playerName = input("\nWhat is your Character's name?: ")
  playerClass = input("Are you a Fighter, Ranger, or Wizard? ")
  playerHP = ((rollDice(6) * rollDice(12)) / 2) + 10
  playerSTR = ((rollDice(6) * rollDice(8)) / 2) + 12
  os.system("clear")
  max_width = max(len(playerName), len(playerClass), len("Strength: " + str(playerSTR)))
  print(playerName)
  print(playerClass)
  print(f"{'HP:':<8}{playerHP:>5}")
  print(f"{'STR:':<8}{playerSTR:>5}")

print("Character Creator!")

while True:
  playerCreator()
  repeat = input("\nWould you like to make another character?: ")
  if repeat.lower() != "yes":
    break