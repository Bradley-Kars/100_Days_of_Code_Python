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

print("Print in Color!\n")

print("With this new subroutine, I can print in colors like", end=" ")
colorPrint("red", "red")
colorPrint("blue", "blue")
colorPrint("none","and")
colorPrint("green", "green", hide_space=True)
colorPrint("none","!", hide_space=True)