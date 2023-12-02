# Todays task was to make the code form day 18 use a randomly generated number.
# As I already did this for day 18, oops, I'll be providing a hader version of yesterday's code instead.
import random

print("Numerical Evidences v2")
number = random.randint(1,1000)
correct = 0
print()
for i in range(1,11):
  number2 = random.randint(1,1000)
  while True:
    try:
        answer = int(input(str(number) + " x " + str(number2) + " = "))
        break
    except ValueError:
        print('Invalid input. Please enter a numeric value for your answer!')
  if answer == number * number2:
    print("Good job!")
    correct += 1
  else:
    print("Good try but the correct answer was", number * number2)
if correct == 10:
  print("Way to go, you got a perfect score!")
  print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
else:
  print("Good try, you got a", correct,"out of 10.")