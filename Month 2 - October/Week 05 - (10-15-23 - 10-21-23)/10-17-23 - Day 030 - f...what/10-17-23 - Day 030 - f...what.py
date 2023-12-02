from getpass import getpass as input

print("Thoughts so far")

for i in range(1,31):
  thoughts = input(f"Day {i: ^3} OF 30: \nWhat were your thoughts on the code I created?: ")
  print(f'You thought day {i} was "{thoughts}"')