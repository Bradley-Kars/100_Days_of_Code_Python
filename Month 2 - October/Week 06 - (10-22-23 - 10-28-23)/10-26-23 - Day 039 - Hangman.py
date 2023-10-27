import nltk
import random
import os

nltk.download("words")
english_words = nltk.corpus.words.words()
word_choices = [word for word in english_words]
random_word = random.choice(word_choices)
os.system("clear")

correctly_guessed = []
guessed = []
tries = 0
wrong_guesses = 0
unique_letters = set(random_word)

def display_hangman(wrong_guesses):
  hangman_parts = ["  |  ", "  O  ", " /|\\ ", "  |  ", " / \\ "]
  for part in hangman_parts[:wrong_guesses]:
      print(part)

print("Let's play Hangman!\n")

for letter in random_word:
    print("_", end=" ")

print()

while True:
  display_hangman(wrong_guesses)
  guess = input("\nGuess a letter: ")
  if len(guess) != 1 or not guess.isalpha():
      print("Please enter a single letter.")
      continue
  os.system("clear")
  guessed.append(guess)
  tries += 1
  found = False
  for letter in random_word:
    if guess.lower() == letter.lower():
      correctly_guessed.append(letter)  # Add correctly guessed letter to the list
      found = True
    if letter in correctly_guessed:
      print(letter, end=" ")
    else:
      print("_", end=" ")
  print("\n\nGuessed letters: " + ", ".join(guessed))  # Print the list of guessed letters
  if not found:
    wrong_guesses += 1
    pass
  if set(correctly_guessed) == unique_letters:
    if wrong_guesses < 5:
      print(f"\nCongratulations, you've guessed all the letters in {tries} tries!")
      break
    else:
      print(f"\nGood try but you lost, you've guessed all the letters in {tries} tries!")
      print()
      display_hangman(wrong_guesses)
      break