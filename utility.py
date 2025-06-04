import os

def clear_console():
  """
  Clears the console screen.
  """
  if os.name == 'nt':
      os.system('cls')  # For Windows
  else:
      os.system('clear')  # For Unix/Linux/Mac
