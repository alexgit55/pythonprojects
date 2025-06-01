import os

def clear_console():
  # Clear console based on the operating system
  if os.name == 'nt':
      os.system('cls')  # For Windows
  else:
      os.system('clear')  # For Unix/Linux/Mac
