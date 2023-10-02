from getpass import getpass as input
valid_choices = ["rock", "paper", "scissors", "r", "p", "s"]
player1 = input("Rock, Paper, Scissors, Shoot!: ").lower()
while player1 not in valid_choices:
    print("Invalid choice. Please choose from 'rock,' 'paper,' or 'scissors.'")
    player1 = input("Rock, Paper, Scissors, Shoot!: ").lower()
player2 = input("Rock, Paper, Scissors, Shoot!: ").lower()
while player2 not in valid_choices:
    print("Invalid choice. Please choose from 'rock,' 'paper,' or 'scissors.'")
    player2 = input("Rock, Paper, Scissors, Shoot!: ").lower()
if player1.lower() == "rock" or player1.lower() == "r":
    if player2.lower() == "rock" or player2.lower() == "r":
        result = "it's a tie!"
        action = "is next to"
    elif player2.lower() == "paper" or player2.lower() == "p":
        result = "player 2 wins!"
        action = "is smothered by"
    else:
        result = "player 1 wins!"
        action = "smashes"
elif player1.lower() == "paper" or player1.lower() == "p":
    if player2.lower() == "rock" or player2.lower() == "r":
        result = "player 1 wins!"
        action = "smothers"
    elif player2.lower() == "paper" or player2.lower() == "p":
        result = "it's a tie!"
        action = "is next to"
    else:
        result = "player 2 wins!"
        action = "is cut to pieces"
elif player1.lower() == "scissors" or player1.lower() == "s":
    if player2.lower() == "rock" or player2.lower() == "r":
        result = "player 2 wins!"
        action = "is shattered by"
    elif player2.lower() == "paper" or player2.lower() == "p":
        result = "player 1 wins!"
        action = "shred"
    else:
        result = "it's a tie!"
        action = "is next to"
print("Player 1's", player1.lower(), action, "by player 2's", player2.lower(), result)