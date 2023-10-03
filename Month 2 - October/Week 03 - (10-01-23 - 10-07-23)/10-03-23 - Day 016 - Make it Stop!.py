count = 1
print("Fillin the blank:")
while True:
  blank = input("Blinded by the light. Cut loose like a _____, another runner in the night.: ")
  if blank.lower() == "deuce":
    if count == 1:
      print("Good job that only took you", count,"try!")
    else:
      print("Good job that only took you", count,"tries!")
    break
  else:
    print("try again!")
    count += 1