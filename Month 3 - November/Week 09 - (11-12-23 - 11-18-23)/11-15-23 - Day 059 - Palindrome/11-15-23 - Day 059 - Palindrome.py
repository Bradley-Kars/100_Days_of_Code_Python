print("Palindrome Detector\n")
palindrome = input("Please input the word or phrase you'd like to test: ")
reversed_palindrome = palindrome[::-1]
reversed_palindrome_check = palindrome.casefold().replace(" ", "")[::-1]
if palindrome.casefold().replace(" ", "") == reversed_palindrome_check:
  print(f"\nYes, '{palindrome}' is a palindrome!")
else:
  print(f"\nNo, '{palindrome}' backwards is '{reversed_palindrome}' and that's not a palindrome.")