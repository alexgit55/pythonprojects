import random
import validation
import utility

#Sets the initial values for core variables in the game
#rpsIcons represent the emjoi's to use for each move
#rpsConditions is a dict showing which move (the key) beats which other move (the value)
#choices is going to be the allowed moves in the game based on the emoji entries
#gameresults stores how many times the game ends with each condition
rpsIcons={"r":"\U0001FAA8","p":"\U0001F5CE","s":"\U00002702"}
rpsConditions={"r":"s","p":"r","s":"p"}
choices=tuple(rpsIcons.keys())
gameResults={"Draw":0,"Player 1":0,"Player 2":0}

def RoundWinner(firstPlayer, secondPlayer):
  """Determines the winner of a single round of Rock, Paper, Scissors.

  Args:
    firstPlayer: The move of the first player (r, p, or s).
    secondPlayer: The move of the second player (r, p, or s).

  Returns:
    "Draw" if the players chose the same move.
    "Player 1" if the first player wins.
    "Player 2" if the second player wins.
  """
  if firstPlayer == secondPlayer:
    return "Draw"
  elif secondPlayer == rpsConditions[firstPlayer]:
    return "Player 1"

  return "Player 2"

def DisplayGameResults(results):
  """Displays the game results.

  Args:
    results: A dictionary containing the game results.
  """
  print("Game Results")
  print("------------")
  for i in results:
    print(f"{i}: {results[i]}")

def PlayComputer():
  """Determines whether the player wants to play against the computer.

  Returns:
    True if the player wants to play against the computer, False otherwise.
  """
  computerRound=validation.ValidateUserInput("Would you like to play against the computer? (y/n): ", ('y','n'))
  if computerRound=='y':
    return True
  return False

def GameRound(computerRound):
  """Plays a single round of Rock, Paper, Scissors.

  Args:
    computerRound: A boolean indicating whether the player is playing against the computer.

  Returns:
    The winner of the round ("Draw", "Player 1", or "Player 2").
  """
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
  """Plays a game of Rock, Paper, Scissors until there is a winner.

  The game consists of multiple rounds. In each round, the players choose their moves,
  and the winner of the round is determined. The first player to win two rounds wins the game.

  Returns:
    The winner of the game ("Draw", "Player 1", or "Player 2").
  """
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
