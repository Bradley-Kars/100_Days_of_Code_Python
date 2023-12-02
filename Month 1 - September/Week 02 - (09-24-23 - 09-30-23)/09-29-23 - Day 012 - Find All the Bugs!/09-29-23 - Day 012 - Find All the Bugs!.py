# Original code:

# print("100 Days of Code QUIZ")
# print()
# print("How many can you answer correctly?)
# - Missing a closing double quotation mark at the end of the string.
# - Missing a space before the closing quotation mark.

# ans1 = ("What language are we writing in?")
# - Missing the input() function to get user input.
# - Added a space after the question mark for better formatting.

# if ans1 == "python":
#   print("Correct")
# else:
#   print("Nope🙈
# - Missing a closing double quotation mark at the end of the "Nope" string.
# - The "if" condition lacks proper input validation.

# ans2 = input("Which lesson number is this?")
# - Missing int() to convert the input to an integer.

# if(ans2>12):
# print("We're not quite that far yet")
# - Indentation issue with the print line.

# else:
#   print("We've gone well past that!")
# - "else" line put before "elif" line.

# elif(ans2==12):
#   print("That's right!")
# - "elif" should be beofre else.

# Corrected code:

print("100 Days of Code QUIZ")
print()
print("How many can you answer correctly? ")
ans1 = input("What language are we writing in? ")
if ans1.lower() == "python":
  print("Correct")
else:
  print("Nope")
ans2 = int(input("Which lesson number is this?"))
if ans2 > 12:
  print("We're not quite that far yet")
elif ans2 == 12:
  print("That's right!")
else:
  print("We've gone well past that!")