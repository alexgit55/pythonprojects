# pythonprojects
Collection of Python Exercises and Projects

This repository contains a collection of exercises and projects I've worked on using Python. 
As the repository grows, I'll keep an updated overview of the projects here

## Utility scripts - Personal scripts that are used to help the main projects

validation
- module containing validation functions to be used in other scripts
* contains function to check if user input matches character in tuple
+ contains function to verify input is a valid integer value

utility
- module containing variety of functions to be used in other scripts
* contains function to clear the output screen

## Mosh's Python Projects - My code for the python projects from Mosh's courses

dice_roller 
- application for rolling a die (random int from 1-6) 
* asks the user for how many times they want to roll
+ continues to prompt until exited by user
+ utilizes validation module to verify input from user
+ prints the number of rolls and how many times each number  came up for the session

number_guessing
- application for guessing a number between a chosen range or a default range
* asks the user if they want to enter the low/high values or use default
+ utilizes validation module to verify input from user
+ limits the number of chances a player gets to guess the number
+ stores game history and prints number of games played and fewest guesses

rock_paper_scissors
- application for playing the rock,paper,scissors game
* can play against the computer with random move selection or with two people and having it prompt for each turn
+ each game winner is determined by best of 3 rounds, it records the winner for reporting at the end
+ game will repeat until user chooses not to, at the end will report how many times each player won a game
+ utilizes validation module to verify input from user
+ utilizes utility module to clear output during the game
