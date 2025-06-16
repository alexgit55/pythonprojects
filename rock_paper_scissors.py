import random
import validation
import utility
import math

class RockPaperScissors:
  #Sets the initial values for core variables in the game
  #rpsIcons represent the emjoi's to use for each move
  #rpsConditions is a dict showing which move (the key) beats which other move (the value)
  #choices is going to be the allowed moves in the game based on the emoji entries
  #gameresults stores how many times the game ends with each condition
  rpsIcons={"r":"\U0001FAA8","p":"\U0001F5CE","s":"\U00002702"}
  rpsConditions={"r":"s","p":"r","s":"p"}
  choices=tuple(rpsIcons.keys())
  gameResults={"Draw":0,"Player 1":0,"Player 2":0}

  def set_game_properties(self):
    """Sets the game properties, including the number of rounds and whether to play against the computer.
    """
    while True:
      rounds=validation.GetIntValue("How Many rounds do you want to play? (must be odd number): ")
      if rounds % 2 ==0:
        print("You must enter an odd number so game winner can be determined.")
        continue
      self.game_rounds=rounds
      self.victory=math.ceil(rounds/2)
      break

    play_Computer=validation.ValidateUserInput("Would you like to play against the computer? (y/n): ", ('y','n'))
    if play_Computer=='y':
      self.play_Computer=True
    else:
      self.play_Computer=False

  def RoundWinner(self, firstPlayer, secondPlayer):
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
    elif secondPlayer == RockPaperScissors.rpsConditions[firstPlayer]:
      return "Player 1"

    return "Player 2"

  def DisplayGameResults(self):
    """Displays the game results.

    Args:
      results: A dictionary containing the game results.
    """
    print("Game Results")
    print("------------")
    for i in RockPaperScissors.gameResults:
      print(f"{i}: {RockPaperScissors.gameResults[i]}")

  def GameRound(self):
    """Plays a single round of Rock, Paper, Scissors.

    Args:
      computerRound: A boolean indicating whether the player is playing against the computer.

    Returns:
      The winner of the round ("Draw", "Player 1", or "Player 2").
    """
    player1Move=validation.ValidateUserInput("Player 1: Rock, paper or scissors? (r/p/s): ",RockPaperScissors.choices)
    if self.play_Computer:
      player2Move=random.choice(RockPaperScissors.choices)
    else:
      utility.clear_console()
      player2Move=validation.ValidateUserInput("Player 2: Rock, paper or scissors? (r/p/s): ",RockPaperScissors.choices)

    utility.clear_console()
    print(f"Player 1 chose {RockPaperScissors.rpsIcons[player1Move]}.")
    print(f"Player 2 chose {RockPaperScissors.rpsIcons[player2Move]}.")

    return self.RoundWinner(player1Move,player2Move)

  def PlayGame(self):
    """Plays the Rock, Paper, Scissors game for a specified number of rounds.

    The game continues until one player wins a majority of the rounds or all rounds are played.
    The game results are updated after each game.
    """
    utility.clear_console()
    roundResults={"Draw":0,"Player 1":0,"Player 2":0}

    for round in range(self.game_rounds):
      print(f"Rock, Paper, Scissors: Round {round+1} of {self.game_rounds}")
      winner=self.GameRound()
      roundResults[winner]+=1
      if winner == "Draw":
        print("It's a draw!")
      else:
        print(f"{winner} wins the round!")

      if roundResults[winner] == self.victory:
        if (winner=="Draw"):
          print("You are evenly matched! Neither one can claim victory")
          break
        else:
          print(f"{winner} wins the game!")
          break
    else:
      print("Oh No! Nobody wins!")
      winner = "Draw"
    RockPaperScissors.gameResults[winner]+=1

playAgain='y'
rps=RockPaperScissors()
while playAgain=='y':
  rps.set_game_properties()
  rps.PlayGame()
  playAgain=validation.ValidateUserInput("Would you like to play again? (y/n): ",('y','n'))
else:
  utility.clear_console()
  print("Thanks for playing!\n")

rps.DisplayGameResults()
