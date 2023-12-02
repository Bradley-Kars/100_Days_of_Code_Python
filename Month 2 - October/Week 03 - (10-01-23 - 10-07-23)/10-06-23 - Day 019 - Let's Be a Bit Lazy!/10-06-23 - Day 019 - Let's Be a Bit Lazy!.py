print("Loan Calculator")
while True:
    try:
        loan = float(input("How much did you borrow?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How much did you borrow?"')
while True:
    try:
        interest = float(input("What is your interest rate?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "What is your interest rate?"')
while True:
    try:
        years = int(input("How many years is the loan for?: "))
        break
    except ValueError:
        print('Invalid input. Please enter numeric values for "How many years is the loan for?"')
annualInterestRate = (interest / 100) + 1
formatted_interest = '{:.2f}%'.format(interest)
counter = 0
print()
print("You took a", years, "year loan of", '${:.2f}'.format(loan), "at an interest rate of", formatted_interest, "APR.")
print("Assuming no payments are made, you'll owe:")
for amountDue in range(years):
  loan = loan * annualInterestRate
  counter += 1
  print("Year", counter, "you owe", '${:.2f}'.format(loan))