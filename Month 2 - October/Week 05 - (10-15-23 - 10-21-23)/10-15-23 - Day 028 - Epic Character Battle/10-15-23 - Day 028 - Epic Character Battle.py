import random
import os
import time

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
  return playerName, playerClass, playerHP, playerSTR

def battleSimulator(player1HP, player1STR, player1Name, player2HP, player2STR, player2Name):
  while player1HP > 0 and player2HP > 0:
    player1Roll = rollDice(6)
    player2Roll = rollDice(6)
    if player1Roll > player2Roll:
      damage = max(player1STR - player2STR + 1, 1)
      print("\n" + player1Name, "did", damage, "damage to", player2Name)
      player2HP = player2HP - damage
    elif  player1Roll < player2Roll:
      damage = max(player2STR - player1STR + 1, 1)
      print("\n" + player2Name, "did", damage, "damage to", player1Name)
      player1HP = player1HP - damage
  time.sleep(3)
  os.system("clear")
  print("And we have a winner!!!\n")
  time.sleep(1)
  player1HP = max(player1HP, 0)
  player2HP = max(player2HP, 0)
  statSheet(player1Name, player1Class, player1HP, player1STR, player2Name, player2Class, player2HP, player2STR)

def statSheet(player1Name, player1Class, player1HP, player1STR, player2Name, player2Class, player2HP, player2STR):
  print(f"{player1Name:<13} {player2Name}")
  print(f"{player1Class:<13} {player2Class}")
  print(f"{'HP:':<8}{player1HP:5} {'HP:':<8}{player2HP:5}")
  print(f"{'STR:':<8}{player1STR:5} {'STR:':<8}{player2STR:5}")

print("Ultimate Battle!")

while True:
  player1Name, player1Class, player1HP, player1STR = playerCreator()
  player2Name, player2Class, player2HP, player2STR = playerCreator()
  time.sleep(3)
  os.system("clear")
  statSheet(player1Name, player1Class, player1HP, player1STR, player2Name, player2Class, player2HP, player2STR)
  print("\nThe battle begins!")
  battleSimulator(player1HP, player1STR, player1Name, player2HP, player2STR, player2Name)
  repeat = input("\nWould you like to make another character?: ")
  if repeat.lower() != "yes":
    break