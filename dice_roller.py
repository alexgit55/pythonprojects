import random
import validation

def DiceRoll():
  """
  Simulates a single dice roll.

  Returns:
      int: A random integer between 1 and 6, representing the result of the dice roll.
  """
  return random.randint(1,6)

def GetDiceRollCount():
  """
  Gets the desired number of dice rolls from the user.

  Returns:
      int: The number of dice rolls the user wants, or 0 to quit.
  """
  playerChoice=-1
  while playerChoice < 0:
      playerChoice=validation.GetIntValue("Enter the number of dice rolls desired: (0 to quit) ")
      if playerChoice < 0:
        print("Value must be 0 or higher.")

  return playerChoice

def DisplayDiceTotals(diceTotals, rollCount):
  """
  Displays the totals for each dice value rolled.

  Args:
      diceTotals (dict): A dictionary containing the count of each dice value (1-6).
      rollCount (int): The total number of dice rolls.
  """
  text="dice"
  if rollCount == 1:
    text="die"
  for i in diceTotals:
    print(f"{i}: {diceTotals[i]}")
  print(f"You rolled {rollCount} {text}")

playAgain='y'
rollList=[]
rollCount=0
diceTotals={1:0,2:0,3:0,4:0,5:0,6:0}

while playAgain=='y':
  rollList.clear()
  numberDiceRolls=GetDiceRollCount()

  if numberDiceRolls == 0:
    break

  for i in range(numberDiceRolls):
    roll=DiceRoll()
    diceTotals[roll] +=1
    rollList.append(roll)
    rollCount+=1

  rollTuple=tuple(rollList)
  print(rollTuple)
  playAgain=validation.ValidateUserInput("Would you like to roll again? (y/n): ",('y','n'))

print("Thanks for playing!")
DisplayDiceTotals(diceTotals, rollCount)
