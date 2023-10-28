website = {"name": None, "url": None, "desc": None, "rating": None}

def get_valid_rating_input():
  while True:
      rating_input = input("rating - Please rate in the format of x/5: ")
      if "/" in rating_input:
          rating_parts = rating_input.split("/")
          if len(rating_parts) == 2:
              try:
                  x = float(rating_parts[0])
                  if 0 <= x <= 5:
                      return rating_input
              except ValueError:
                  pass
      print("Invalid rating format. Please use x/5 format with x between 0 and 5.")

for name in website.keys():
  if name == "name":
    name_input = input(f"{name} - please enter the name of the website: ")
    website[name] = name_input
  elif name == "url":
    url_input = input(f"{name} - please enter the URL of the website: ")
    website[name] = url_input
  elif name == "desc":
    desc_input = input(f"{name} - please enter the description of the website: ")
    website[name] = desc_input
  elif name == "rating":
    website[name] = get_valid_rating_input()
  else:
    website[name] = input(f"{name}: ")

print()

for name, value in website.items():
  if name == "rating":
    if value == "5/5":
      print(f"{name}: {value}\nThats a great site!")
    elif value == "4/5":
      print(f"{name}: {value}\nThats a solid site!")
    elif value == "3/5":
      print(f"{name}: {value}\nWhy are you using this?")
    elif value == "2/5":
      print(f"{name}: {value}\nThis site seems very subpar")
    elif value == "1/5":
      print(f"{name}: {value}\nThis site really shouldnt exist")
    elif value == "0/5":
      print(f"{name}: {value}\nThis site may be down right dangerous!")
  else:
    print(f"{name}: {value}")