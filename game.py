"""
------------------------------------------------------------------------------------------
File:    game.py
Project: hangman
Purpose: Playing the hangman game
==========================================================================================

Program Description:
  This program simulates the game, hangman
------------------------------------------------------------------------------------------
Author:  Lovette Oyewole
Email:   lovette.oyewole@icloud.com
Version  2021-01-08
-------------------------------------
"""
import time
DASH = '_'
# words for each category
genres = {
		1 : 'spider-man',
		2 : 'drake',
		3 : 'scandal',
		4 : 'vlone',
		5 : 'york',
		6 : 'purple',
		7 : 'grater',
		8 : 'rust',
		9 : 'wales',
		10 : 'locs'
		 }


def Game_Sim(category, turns):
    
    # printing out dashes to get the number of words user has to guess
    for i in range(len(genres[category])):
        print("_", end = " ")
    print("\n\n")
    
    
    word = genres[category] # getting word from dictionary
    user_guesses = "" # string of user guesses
    guess_letter = "" 
    win_count = False
    
    while turns >0 and (not win_count):
        wrong = 0

        if not win_count: # if u haven't won
            guess_letter = input("\nGuess a letter: ") 
            user_guesses += guess_letter # appending the guess into the guesses string
            
            if guess_letter not in word:
                turns -= 1 # decreases the number of chances u get
                print("Sorry, wrong guess")
            time.sleep(0.5)
                
        for char in word:
            
            # prints the right letters the user has guessed
            if char in user_guesses:
                print(char)
                
            else:
                print("_")
                wrong +=1
        
        if wrong == 0:
            win_count = True   #changes to true when all word matches
    
    #final output to screen
    print("\n")  
    if win_count:
        print("*****************************")
        print("\nCONGRATULATIONS!!!!!") 
        print("YOU WON\n")
        print("*****************************")    
            
    else:
        print("*****************************")
        print("\n :( You lost...") 
        print("Try again next time\n")
        print("*****************************")
            
    
    return



#def GuessGetter():

















