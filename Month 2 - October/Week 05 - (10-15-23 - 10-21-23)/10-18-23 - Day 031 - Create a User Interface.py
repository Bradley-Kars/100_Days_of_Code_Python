def colorPrint(color, word, hide_space=False):
  if color == "black":
      return "\033[30m" + word + "\033[0m"
  elif color == "red":
      return "\033[31m" + word + "\033[0m"
  elif color == "green":
      return "\033[32m" + word + "\033[0m"
  elif color == "yellow":
      return "\033[33m" + word + "\033[0m"
  elif color == "blue":
      return "\033[34m" + word + "\033[0m"
  elif color == "magenta":
      return "\033[35m" + word + "\033[0m"
  elif color == "cyan":
      return "\033[36m" + word + "\033[0m"
  elif color == "white":
      return "\033[37m" + word + "\033[0m"
  else:
      return "\033[0m" + word + "\033[0m"

title = f"{colorPrint('red', '=')}{colorPrint('white', '=')}{colorPrint('blue', '=')} {colorPrint('yellow', 'Music App')} {colorPrint('blue', '=')}{colorPrint('white', '=')}{colorPrint('red', '=')}"

print(f"       {title:^25}")

line1 = f"{colorPrint('white', '🔥▶️', hide_space=True):<13}{colorPrint('white', 'Radio Gaga', hide_space=True):^23}"
line2 = f"{colorPrint('yellow', 'Queen'):^27}"

print(line1)
print(line2)
print()

left_text = "prev"
center_text = "next"
right_text = "pause"

total_width = 25

left_formatted = f"{colorPrint('white', left_text):<25}"
center_formatted = f"{colorPrint('green', center_text, hide_space=True):^25}"
right_formatted = f"{colorPrint('magenta', right_text, hide_space=True):>25}"

print(left_formatted)
print(center_formatted)
print(right_formatted)

print()
print()

print(f"{colorPrint('white', 'WELCOME TO', hide_space=True):^35}")
print(f"{colorPrint('blue', '--  ARMBOOK  --', hide_space=True):^35}")
print()
print(f"{colorPrint('yellow', 'Definitely not a rip off', hide_space=True): >35}")
print(f"{colorPrint('yellow', 'a certain other social', hide_space=True): >35}")
print(f"{colorPrint('yellow', 'networking site', hide_space=True): >35}")
print()
print(f"{colorPrint('red', 'Honest.', hide_space=True):^35}")
print()
print(f"{colorPrint('white', 'Username: ', hide_space=True):^35}")
print(f"{colorPrint('white', 'Password: ', hide_space=True):^35}")