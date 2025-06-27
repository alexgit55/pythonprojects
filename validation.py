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

  if not hasattr(validChoices, '__iter__'):
    raise TypeError("ValidChoices must be iterable")

  userChoice = 'userChoice'
  while userChoice.lower() not in validChoices:
    userChoice = input(text)
    if userChoice.lower() in validChoices:
      break
    print("That is not a valid choice")

  return userChoice.lower()


def GetIntValue(text, min=0, max=100):
  """
  Prompts the user for an integer value until a valid integer value is entered.

  Args:
    text: The prompt to display to the user.

  Returns:
    The integer value entered by the user.
  """
  while True:
    try:
      intValue = int(input(f"{text}"))
      assert intValue >= min and intValue <= max
      break
    except ValueError:
      print("That is not a valid number")
    except AssertionError:
      print(f"Value must be between {min} and {max} ")

  return intValue


if __name__ == '__main__':
  userInput = ValidateUserInput(
      "Please select from the following choices (y/n): ", ('y', 'n'))
  print(userInput)

  userInt = GetIntValue("Enter a value to verify functionality: ")
  print(userInt)
