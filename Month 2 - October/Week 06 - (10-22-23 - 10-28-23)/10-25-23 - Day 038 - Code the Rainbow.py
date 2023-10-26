print("Rainbow print!")
print()
sentence = input("What would you like to print in rainbow format?: ")
current_color = "\033[0m"

for letter in sentence:
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