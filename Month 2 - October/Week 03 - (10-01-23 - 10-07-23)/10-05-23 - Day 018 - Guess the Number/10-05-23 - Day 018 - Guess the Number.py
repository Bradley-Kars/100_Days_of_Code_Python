import random
number = random.randint(1, 1000000)
count = 1
while True:
    try:
        guess = int(input("Guess a number between 1 and 1,000,000: "))
        if guess < 0:
          exit()
        elif guess not in range(1, 1000001):
          print("Invalid choice. Please enter a number between 1 and 1,000,000")
          continue
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        continue
    if guess < number:
        print("Too low!")
        count += 1
    elif guess > number:
        print("Too High!")
        count += 1
    else:
        if count == 1:
            print("You got it and it only took you", count, "try!")
        else:
            print("You got it and it only took you", count, "tries!")
        break