winCount1 = 0
winCount2 = 0
while True:
  if winCount1 < 3 and winCount2 < 3:
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
            winCount2 += 1
        else:
            result = "player 1 wins!"
            action = "smashes"
            winCount1 += 1
    elif player1.lower() == "paper" or player1.lower() == "p":
        if player2.lower() == "rock" or player2.lower() == "r":
            result = "player 1 wins!"
            action = "smothers"
            winCount1 += 1
        elif player2.lower() == "paper" or player2.lower() == "p":
            result = "it's a tie!"
            action = "is next to"
        else:
            result = "player 2 wins!"
            action = "is cut to pieces"
            winCount2 += 1
    elif player1.lower() == "scissors" or player1.lower() == "s":
        if player2.lower() == "rock" or player2.lower() == "r":
            result = "player 2 wins!"
            action = "is shattered by"
            winCount2 += 1
        elif player2.lower() == "paper" or player2.lower() == "p":
            result = "player 1 wins!"
            action = "shred"
            winCount1 += 1
        else:
            result = "it's a tie!"
            action = "is next to"
    print("Player 1's", player1.lower(), action, "by player 2's", player2.lower(), result)
  else:
    if winCount1 > winCount2:
      winner = "Player 1"
    elif winCount2 > winCount1:
      winner = "Player 2"
    print("We have a winner! Player 1 got", winCount1, "while player 2 got", winCount2, "that makes", winner, "our champion!")
    break