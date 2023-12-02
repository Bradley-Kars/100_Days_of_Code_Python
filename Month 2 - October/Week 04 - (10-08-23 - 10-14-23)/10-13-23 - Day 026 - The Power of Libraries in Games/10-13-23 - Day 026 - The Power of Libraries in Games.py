from replit import audio
import os

def play():
  source = audio.play_file('audio.wav')
  source.paused = False

def menu():
  print("Music Player")
  while True:
    userInput = input("Press 1 to Play\nPress 2 to exit\n")
    if userInput == "1":
      print("Now PLaying!")
      play()
    elif userInput == "2":
      exit()
    else :
      continue

if __name__ == "__main__":
  while True:
    os.system("clear")
    menu()