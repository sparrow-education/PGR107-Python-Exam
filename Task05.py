"""
-----------------------------------------
PGR107 Eksam                            #
Task 5                                  #
Group: PGR107_Students_2023             #
Description: Guess a word game          #
-----------------------------------------
"""
# libraries 
import random

## function for opne file
def handle_file(filtype):
    
    with open(filtype, "r") as file:
        scan_words = file.readlines()
    return random.choice(scan_words).strip()
 
## function for displying words in terminal    
def displaying_words(word, guessed_letters):
    
    show_display = ""
    for letter in word:
        if letter in guessed_letters:
            show_display += letter
        else: 
            show_display += "_"
    return show_display

## main function to play the-game
def play_game():
    while True:
        try:
            filtype = input("Enter the filename containing the words (e.x..words.txt):\n>>")
            word = handle_file(filtype) 
            break
            
        except Exception  as e:
            print(f"Error: {e}. Please try again with valid filename\n")
            
    guessed_letters = set() 
    incorrect_guess = 0 
    word_length = len(word)
    
    ## display of instrcutions and menu
    print("          __        ___  __   __  ")
    print("|  |     / _` |  | |__  /__` /__` ")
    print("|/\| ___ \__> \__/ |___ .__/ .__/ ")
    print("                                  ")
    print("Version 1.0")
    print("\n")
    print(f"Welcome to the guessing game\n"
    f"Type \q command to leave the game early\n\n")
    print("-" * 75)
    print(f"The word you need to guess has {word_length} characters. "
    f"You have {word_length} guesses left.\n")
    
    
    while incorrect_guess < word_length: 
        print("Current word:" , displaying_words(word, guessed_letters)) 
        sGuess = input("Guess a character: ").lower()
        
        ## check to quit the game after 
        if sGuess == '\\q':
            print("Exiting game..")
            break
            
        ## check to warn the user to only add only a singe letter
        
        if not sGuess.isalpha() or len(sGuess) > 1:
            print("Please enter a single letter only.\n")
            continue
        
        if sGuess in guessed_letters:
            print("You already guessed this letter\n")
        
        elif sGuess in word:
            guessed_letters.add(sGuess)
            print("Correct letter\n")
            print("-" * 55)
        
        else:
            incorrect_guess += 1
            print("-" * 55)
            print(f"Sorry, incorrect letter. You have {word_length - incorrect_guess} guesses left.") 
            
        if set(word).issubset(guessed_letters):
            print(f"Congratulations! You guessed the word: {word}")
            break
    else:
        print(f"Game over! The word was: {word}")


play_game()        

##------- End_of_Program ---------- ##
        
            
    

    

