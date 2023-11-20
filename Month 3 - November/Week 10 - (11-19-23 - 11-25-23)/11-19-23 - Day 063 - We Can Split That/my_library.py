import random

def rollDice(sides):
  roll = random.randint(1,sides)
  print(roll)

def colorPrint(color, word, hide_space=False):
  if color == "black":
    print("\033[30m", word, sep="", end=" " if not hide_space else "")
  elif color == "red":
    print("\033[31m", word, sep="", end=" " if not hide_space else "")
  elif color == "green":
    print("\033[32m", word, sep="", end=" " if not hide_space else "")
  elif color == "yellow":
    print("\033[33m", word, sep="", end=" " if not hide_space else "")
  elif color == "blue":
    print("\033[34m", word, sep="", end=" " if not hide_space else "")
  elif color == "magenta":
    print("\033[35m", word, sep="", end=" " if not hide_space else "")
  elif color == "cyan":
    print("\033[36m", word, sep="", end=" " if not hide_space else "")
  elif color == "white":
    print("\033[37m", word, sep="", end=" " if not hide_space else "")
  else:
    print("\033[0m", word, sep="", end=" " if not hide_space else "")

def rainbowPrint(sentence):
  for letter in sentence:
    current_color = ""
    if letter.lower() == "r":
      current_color = "\033[31m"
    elif letter.lower() == "g":
      current_color = "\033[32m"
    elif letter.lower() == "y":
      current_color = "\033[33m"
    elif letter.lower() == "b":
      current_color = "\033[34m"
    elif letter.lower() == "m":
      current_color = "\033[35m"
    elif letter.lower() == "c":
      current_color = "\033[36m"
    elif letter.lower() == "w":
      current_color = "\033[37m"
    print(current_color, end="")
    print(letter, end="")
  print("\033[0m")