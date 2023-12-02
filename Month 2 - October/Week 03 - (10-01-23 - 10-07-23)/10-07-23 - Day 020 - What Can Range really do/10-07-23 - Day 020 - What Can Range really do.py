print("Number Generator")
print()
while True:
    try:
        start = int(input("Starting number: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How much did you borrow?"')
while True:
    try:
        end = int(input("End before: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How much did you borrow?"')
while True:
    try:
        increment = int(input("Increment by: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How much did you borrow?"')
print()
for i in range(start, end, increment):
  print(i)