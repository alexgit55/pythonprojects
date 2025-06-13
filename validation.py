#!/usr/bin/env python3

"""validation.py contains validation functions to be used to verify input data from the user"""

def ValidateUserInput(text, validChoices):
  """
  Prompts the user for input until a valid choice from the provided list is entered.

  Args:
    text: The prompt to display to the user.
    validChoices: A list of valid choices (strings).

  Returns:
    The user's choice (string, lowercased).
  """
  userChoice='userChoice'
  while userChoice.lower() not in validChoices:
    userChoice=input(text)
    if userChoice.lower() in validChoices:
      break
    print("That is not a valid choice")

  return userChoice.lower()

def GetIntValue(text):
  """
  Prompts the user for an integer value until a valid integer value is entered.

  Args:
    text: The prompt to display to the user.

  Returns:
    The integer value entered by the user.
  """
  while True:
    try:
        intValue=int(input(f"{text}"))
        break
    except ValueError:
        print("That is not a valid number")

  return intValue
