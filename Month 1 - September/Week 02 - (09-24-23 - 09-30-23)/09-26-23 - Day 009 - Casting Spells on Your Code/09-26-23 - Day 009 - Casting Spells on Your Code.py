print("Generation Identifier")
print()
birthYear = None
while birthYear is None:
    birthYear_input = input("Please enter the year you were born (e.g., 1990): ")
    try:
        birthYear = int(birthYear_input)
    except ValueError:
        print("Please enter your birth year as a valid four-digit number (e.g., 1990).")
if birthYear < 1901:
  print("I think we found the Lost Generation!")
elif birthYear < 1928:
  print("Whats so great about the Greatest Generation again?")
elif birthYear < 1946:
  print("Dont worry we didn't forget about the Silent Generation.")
elif birthYear < 1965:
  print("BOOMER")
elif birthYear < 1981:
  print("Generation X gon' give it to ya")
elif birthYear < 1997:
  print("Hello fellow Millennials!")
elif birthYear < 2013:
  print("Zoomer")
else:
  print("who let Gen Alpha online... y'all scary.")