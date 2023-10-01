print("Grade Calculator")
print()
examName = input("Name of exam: ")
print()
while True:
    try:
        perfectScore = float(input("Best possible score: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "best possible score"')
print()
while True:
    try:
        yourScore = float(input("Your score: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "your score"')

percentage = yourScore/perfectScore
percentage_string = "{:.2f}%".format(percentage * 100)
if 0.93 <= percentage:
    grade = "A"
    color = "\033[0;32m"
elif 0.90 <= percentage <= 0.92:
    grade = "A-"
    color = "\033[0;32m"
elif 0.87 <= percentage <= 0.89:
    grade = "B+"
    color = "\033[0;32m"
elif 0.83 <= percentage <= 0.86:
    grade = "B"
    color = "\033[0;93m"
elif 0.80 <= percentage <= 0.82:
    grade = "B-"
    color ="\033[0;93m"
elif 0.77 <= percentage <= 0.79:
    grade = "C+"
    color = "\033[0;93m"
elif 0.73 <= percentage <= 0.76:
    grade = "C"
    color = "\033[0;93m"
elif 0.70 <= percentage <= 0.72:
    grade = "C-"
    color = "\033[0;31m"
elif 0.67 <= percentage <= 0.69:
    grade = "D+"
    color = "\033[0;31m"
elif 0.60 <= percentage <= 0.66:
    grade = "D"
    color = "\033[0;31m"
else:
    grade = "F"
    color = "\033[0;31m"
print(color)
print("Looks like you got a", percentage_string, "which is a", str(grade), "on your" , examName, "assignment!")