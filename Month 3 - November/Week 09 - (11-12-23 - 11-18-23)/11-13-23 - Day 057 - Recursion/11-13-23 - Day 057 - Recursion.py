print("Factorial Calculator")

def factorial(value):
  global factorial_output
  if value <= 1:
    print(f"{user_input} factorial is {factorial_output}")
    return
  else:
    factorial_output = factorial_output * (value - 1)
    factorial(value-1)

while True:
  try:
    user_input = int(input("What number would you like to find the factorial of?: "))
    break
  except ValueError:
    print("Please enter a valid integer.")
    
factorial_output = user_input
factorial(user_input)