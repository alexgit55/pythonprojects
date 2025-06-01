import random
import validation
import utility

rpsIcons={"r":"\U0001FAA8","p":"\U0001F5CE","s":"\U00002702"}
rpsConditions={"r":"s","p":"r","s":"p"}
choices=tuple(rpsIcons.keys())
gameResults={"Draw":0,"Player 1":0,"Player 2":0}

def RoundWinner(firstPlayer, secondPlayer):
  if firstPlayer == secondPlayer:
    return "Draw"
  elif secondPlayer == rpsConditions[firstPlayer]:
    return "Player 1"

  return "Player 2"

def DisplayGameResults(results):
  print("Game Results")
  print("------------")
  for i in results:
    print(f"{i}: {results[i]}")

def PlayComputer():
  computerRound=validation.ValidateUserInput("Would you like to play against the computer? (y/n): ", ('y','n'))
  if computerRound=='y':
    return True
  return False

def GameRound(computerRound):
  player1Move=validation.ValidateUserInput("Player 1: Rock, paper or scissors? (r/p/s): ",choices)
  if computerRound:
    player2Move=random.choice(choices)
  else:
    utility.clear_console()
    player2Move=validation.ValidateUserInput("Player 2: Rock, paper or scissors? (r/p/s): ",choices)

  utility.clear_console()
  print(f"Player 1 chose {rpsIcons[player1Move]}.")
  print(f"Player 2 chose {rpsIcons[player2Move]}.")

  return RoundWinner(player1Move,player2Move)

def PlayGame():
  utility.clear_console()
  roundResults={"Draw":0,"Player 1":0,"Player 2":0}
  computerRound=PlayComputer()

  for round in range(3):
    print(f"Rock, Paper, Scissors: Round {round+1} of 3")
    winner=GameRound(computerRound)
    if winner == "Draw":
      print("It's a draw!")
    else:
      print(f"{winner} wins the round!")
      roundResults[winner]+=1

    if roundResults[winner] == 2:
      print(f"{winner} wins the game!")
      return winner
  else:
    print("Oh No! Nobody wins!")
    return "Draw"

playAgain='y'
while playAgain=='y':
  gameWinner=PlayGame()
  gameResults[gameWinner]+=1
  playAgain=validation.ValidateUserInput("Would you like to play again? (y/n): ",('y','n'))
else:
  utility.clear_console()
  print("Thanks for playing!\n")

DisplayGameResults(gameResults)
