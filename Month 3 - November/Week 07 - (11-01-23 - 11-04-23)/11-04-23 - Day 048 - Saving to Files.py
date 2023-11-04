print("Score Board")

f = open("high_score.txt", "a+")

while True:
  while True:
    initials = input("Please enter your initials: ").upper()
    if len(initials) == 3 and initials.isalpha():
        break
    else:
        print("Invalid input. Please enter 3 letters as your initials.")
  while True:
    try:
        score_input = int(input("Please enter your score: "))
        if 0 <= score_input <= 999999:
            break
        else:
            print("Invalid input. Please enter a number between 0 and 999,999.")
    except ValueError:
        print("Invalid input. Please enter a valid number between 0 and 999,999.")
  f.write(f"{initials} {score_input}\n")
  keep_going = input("Do you have another score to input?: ")
  if keep_going != "yes":
    break

f.close()