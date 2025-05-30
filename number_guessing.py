import random
import validation

def GenerateRandomNumber(lowValue, highValue):
  return random.randint(lowValue, highValue)

def SetNumberRange():
  manualRange = validation.ValidateUserInput("Would you like to set the number range? If not, range will be 1-100 (y/n): ",('y','n'))
  lowValue=0
  highValue=-1

  if manualRange=='y':
    while lowValue > highValue:
      lowValue=validation.GetIntValue("Enter number for the low value: ")
      highValue=validation.GetIntValue("Enter number for the high value: ")

      if highValue < lowValue:
        print("The high value must be greater than the low value.")
  else:
    lowValue=1
    highValue=100

  return (lowValue, highValue)

def PlayGame(numberToGuess, maxTurns, gameHistory):
  count=0
  while maxTurns > 0:
    if maxTurns == 1:
      print("This is your last guess!")
    else:
      print(f"You have {maxTurns} guesses remaining")
    userGuess=validation.GetIntValue("What is your guess? ")
    count += 1
    if userGuess == numberToGuess:
      print(f"You got it! The number was {numberToGuess}")
      print(f"You guessed the number in {count} attempts.")
      gameHistory.append(count)
      break
    maxTurns -= 1
    if maxTurns == 0:
      print(f"Oh no! You ran out of guesses. The correct number was {numberToGuess}")
      break
    if userGuess < numberToGuess:
      print("Too low! Try again")
    else:
      print("Too high! Try again")

gameHistory=[]
maxTurns=10
playAgain='y'
while playAgain=='y':
  low,high=SetNumberRange()
  numberToGuess=GenerateRandomNumber(low, high)
  PlayGame(numberToGuess,maxTurns,gameHistory)
  playAgain=validation.ValidateUserInput("Would you like to play again? (y/n): ",('y','n'))

print("Thanks for playing!")
if len(gameHistory) == 1:
  endText="time"
else:
  endText="times"
print(f"You played {len(gameHistory)} {endText}.")
print(f"Your best attempt was {min(gameHistory)} guesses.")
