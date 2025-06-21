import random
import validation
import utility

class NumberGuessingGame:
  """
  A class that implements a number guessing game.

  The game generates a random number within a specified range,
  and the player has a limited number of turns to guess the number.
  The game provides feedback on whether the guess is too high or too low.
  """
  def __init__(self):
    self.__number_to_guess=0
    self.__max_turns=10
    self.__game_history=[]
    self.__low_range=1
    self.__high_range=100
    self.GameIntro()

  def GameIntro(self):
    """Displays introductory message to player when launching game for the first time"""
    
    print("Welcome to the number guessing game!")
    print(f"I will generate a random number between a range and you will have {self.__max_turns} turns to guess it.")
    print("The default range will be from 1 to 100.")
           
  def SetNumberRange(self):
    """
    Allows the player to manually set the number range for the guessing game.

    If the player chooses to set the range manually, they are prompted to enter
    the low and high values for the range. Input validation is performed to
    ensure that the high value is greater than the low value. If the player
    chooses not to set the range manually, the default range of 1 to 100 is used.
    """
  
    manualRange = validation.ValidateUserInput("Would you like to set the number range? If not, range will be 1-100 (y/n): ",('y','n'))
    lowValue=1
    highValue=0
    
    if manualRange=='y':
      while lowValue > highValue:
        lowValue=validation.GetIntValue("Enter number for the low value: ",max=100000)
        highValue=validation.GetIntValue("Enter number for the high value: ",min=lowValue+1,max=1000000)

        if highValue < lowValue:
          print("The high value must be greater than the low value.")
    else:
      lowValue=1
      highValue=100

    self.__low_range=lowValue
    self.__high_range=highValue
    
  def GenerateRandomNumber(self):
    """
    Generates a random integer between the specified low and high values (inclusive).
    """
    self.__number_to_guess=random.randint(self.__low_range, self.__high_range)

  def PlayRound(self):
    """
    Initiates and manages a single round of the number guessing game.

    The player is prompted to enter their guess, and the game provides
    feedback on whether the guess is too high or too low. The number of
    attempts is tracked, and the game continues until the player guesses
    the correct number or runs out of turns.
    """
   
    count=0
    maxTurns=self.__max_turns
    while maxTurns > 0:
      if maxTurns == 1:
        print("This is your last guess!")
      else:
        print(f"You have {maxTurns} guesses remaining")
      userGuess=validation.GetIntValue("What is your guess? ")
      count += 1
      if userGuess == self.__number_to_guess:
        print(f"You got it! The number was {self.__number_to_guess}")
        print(f"You guessed the number in {count} attempts.")
        self.__game_history.append(count)
        break
      maxTurns -= 1
      if maxTurns == 0:
        print(f"Oh no! You ran out of guesses. The correct number was {self.__number_to_guess}")
        break
      if userGuess < self.__number_to_guess:
        print("Too low! Try again")
      else:
        print("Too high! Try again")

  def PlayGame(self):
    """
    This method contains the core game logic for the number guessing game.

    It sets the number range, generates a random number, and manages the
    game rounds until the player chooses to stop playing. After each game,
    it displays statistics to the player.
    """
    
    play_again='y'
    while play_again=='y':
      self.SetNumberRange()
      self.GenerateRandomNumber()
      self.PlayRound()
      play_again=validation.ValidateUserInput("Would you like to play again? (y/n): ",('y','n'))
      utility.clear_console()
    else:
      self.DisplayStats()

  def DisplayStats(self):
    """
    Displays game statistics to the player, including the number of times played
    and the best (minimum) number of guesses achieved in a single game.
    """
    
    print("Thanks for playing!")
    if len(self.__game_history) == 1:
      endText="time"
    else:
      endText="times"
    print(f"You played {len(self.__game_history)} {endText}.")
    print(f"Your best attempt was {min(self.__game_history)} guesses.")
    
my_game=NumberGuessingGame()
my_game.PlayGame()
