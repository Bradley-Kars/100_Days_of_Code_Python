print("Star Wars Name Generator")

firstName = input("Enter your first name: ").title()
lastName = input("Enter your last name: ").lower()
maidenName = input("Enter your mothers maiden name: ").title()
homeTown = input("Enter your home town: ").lower()
print(f"{firstName[0:3]}{lastName[0:2]} {maidenName[0:2]}{homeTown[-3:]}")