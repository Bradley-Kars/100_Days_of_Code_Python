print("Numerical Evidences")
print()
while True:
    try:
        number = int(input("Provide a number for your multiplication table: "))
        break
    except ValueError:
        print('Invalid input. Please enter a numeric value for "Provide a number for your multiplication table"')
print()
correct = 0
for i in range(1,11,1):
  while True:
    try:
        answer = int(input(str(i) + " x " + str(number) + " = "))
        break
    except ValueError:
        print('Invalid input. Please enter a numeric value for your answer!')
  if answer == i * number:
    print("Good job!")
    correct += 1
  else:
    print("Good try but the correct answer was", i * number)
if correct == 10:
  print("Way to go, you got a perfect score!")
  print("🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳🥳")
else:
  print("Good try, you got a", correct,"out of 10.")