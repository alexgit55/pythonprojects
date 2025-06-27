#!/usr/bin/env python3
"""utility.py contains custom functions to be used in other scripts/modules"""

import os
import tkinter as tk
from tkinter import filedialog

def clear_console():
  """
  Clears the console screen.
  """
  if os.name == 'nt':
      os.system('cls')  # For Windows
  else:
      os.system('clear')  # For Unix/Linux/Mac

def select_folder(title="Select Folder"):
    """
    Opens a folder selection dialog and returns the selected folder path.
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    folder_path = filedialog.askdirectory(title=title)
    return folder_path
