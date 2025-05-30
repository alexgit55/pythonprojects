def ValidateUserInput(text, validChoices):
  userChoice='userChoice'
  while userChoice.lower() not in validChoices:
    userChoice=input(text)
    if userChoice.lower() in validChoices:
      break
    print("That is not a valid choice")

  return userChoice.lower()

def GetIntValue(text):
  while True:
    try:
        intValue=int(input(f"{text}"))
        break
    except ValueError:
        print("That is not a valid number")

  return intValue
