import random
import validation

def DiceRoll():
  return random.randint(1,6)

def GetDiceRollCount():
  playerChoice=-1
  while playerChoice < 0:
      playerChoice=validation.GetIntValue("Enter the number of dice rolls desired: (0 to quit) ")
      if playerChoice < 0:
        print("Value must be 0 or higher.")

  return playerChoice

def DisplayDiceTotals(diceTotals):
  for i in diceTotals:
    print(f"{i}: {diceTotals[i]}")

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
text="dice"
if rollCount == 1:
  text="die"

DisplayDiceTotals(diceTotals)
print(f"You rolled {rollCount} {text}")
