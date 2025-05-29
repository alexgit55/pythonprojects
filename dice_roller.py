import random

def DiceRoll():
  return random.randint(1,6)

def ContinueGame():
  validChoices='y','n'
  userChoice='a'
  while userChoice.lower() not in validChoices:
    userChoice=input("Would you like to roll again? (y/n): ")
    if userChoice.lower() in validChoices:
      break
    print("Please enter either y or n")

  if userChoice.lower() == 'y':
    return True
  else:
    return False

def GetDiceRollCount():
  playerChoice=-1
  while playerChoice < 0:
    try:
        playerChoice=int(input("Enter the number of dice rolls desired: (0 to quit) "))
    except TypeError:
        print("Please enter a valid number")
  return playerChoice

def DisplayDiceTotals(diceTotals):
  for i in diceTotals:
    print(f"{i}: {diceTotals[i]}")

playAgain=True
rollList=[]
rollCount=0
diceTotals={1:0,2:0,3:0,4:0,5:0,6:0}

while playAgain:
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
  playAgain=ContinueGame()

print("Thanks for playing!")
text="dice"
if rollCount == 1:
  text="die"

DisplayDiceTotals(diceTotals)
print(f"You rolled {rollCount} {text}")
