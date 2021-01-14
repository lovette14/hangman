"""
------------------------------------------------------------------------------------------
File:    main.py
Project: hangman
Purpose: main file for hangman game
==========================================================================================

Program Description:
  This program gets category for user and also simulates the game
------------------------------------------------------------------------------------------
Author:  Lovette Oyewole
Email:   lovette.oyewole@icloud.com
Version  2021-01-08
-------------------------------------
"""
import game # gettting everything from the game.py file
import time
# output to screen
print ("Welcome to the Hangman Game\n")

#categories you can choose from
print("1 - Movie\n"
	"2 - Artist\n"
	"3 - Tv Show\n"
	"4 - Brand (Clothing)\n"
	"5 - Ontario University\n"
	"6 - Colour\n"
	"7 - Cooking Utensil\n"
	"8 - Programming Language\n"
	"9 - Country\n"
	"10 - Hairstyle\n")

# getting user input
category = int(input("Choose a category: "))
turns = int(input("Enter how many chances you would like: "))

print("\n\n===============================")
print("===============================")
print("Starting Game...")
time.sleep(0.5)
print("\nYou have only {:d} chances to enter a wrong letter. Good luck\n".format(turns))
time.sleep(0.5)


Game_Sim(category, turns)
