print("Tip Calculator")
print()
myBill = float(input("What was the bill?: "))
tipPercent = int(input("What percentage would oyu like to tip?: ")) /100
numberOfPeople = int(input("How many people?: "))
totalBill = myBill + myBill * tipPercent
answer = totalBill / numberOfPeople
answer = round(answer, 2)
print(f"You all owe ${answer:.2f}")