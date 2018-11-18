#welcome to my code sir. 
from os import system
#I explained in the lesson the function of this import command. 

#these functions all return something necessary for the larger 'hangman' function to use, for example whether or not the secret word has been guessed / displaying guessed words. 

def isWordGuessed(secretWord, lettersGuessed):
    count=0
    for letters in secretWord:
        if letters in lettersGuessed:
            count+=1
    if count==len(secretWord):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    string=""
    for key in secretWord:
        if key in lettersGuessed:
            string+=key
        else:
            string+=" _ "
    return string

def getAvailableLetters(lettersGuessed):
    string=""
    count=0
    s='abcdefghijklmnopqrstuvwxyz'
    for letter in s:
        if letter in lettersGuessed:
            count+=1
        else:
            string+=letter
    return string    

#this is the main function which controls the entirety of the game. It contains all the ascii and does all of the main logic and syntax. 
def hangman(secretWord):
    chances= 6
    length=len(secretWord)
    print("Welcome to my Hangman game! \n" )
    print("I am thinking of a word that is",length, "letters long. \n")
    lettersGuessed=[]
    while (chances!=0):
        if chances == 6:            
            print("""
    __________
    |/       |
    |        |     
    |                
    |                 
    |               
    |                   
    |_____                 
    """)
            print()
    
        if chances == 5:
            print("""
    __________
    |/       |                         
    |        |   
    |       (_)  
    |                 
    |               
    |                   
    |_____                 
    """)
            print()

        if chances == 4:
            print("""
    __________
    |/       |
    |        |     
    |       (_)       
    |        |       
    |               
    |                   
    |_____                 
    """)
            print()

        if chances == 3:
             print("""
    __________
    |/       |
    |        |     
    |       (_)        
    |        |           
    |        |     
    |          
    |                   
    |_____                 
    """)
             print()
             
        if chances == 2:
            print("""
    __________
    |/       |
    |        |     
    |       (_)      
    |        |         
    |       /|\ 
    |                  
    |_____                 
    """)
            print()
        
        if chances == 1:
            print("""
    __________
    |/       |
    |        |     
    |       (_)       
    |        |         
    |       /|\  
    |       /       
    |_____ /               
    """)
    #Ascii art above gets displayed as a sort of basic image. 
            print()          
        if secretWord!=getGuessedWord(secretWord, lettersGuessed):
            print()
            print("You have", chances, "guesses left.")
            print()
            print("Available letters: ",getAvailableLetters(lettersGuessed))
            print()
            guess=input("Please guess a letter: ")
            guessInLowerCase = guess.lower()
            while not guess.isalpha():
                print("Please use a letter, specifically from the avaliable letters above. \n")
                guess = input("Choose a letter- \n") 
            while len(guess) != 1:
                if len(guess) > 1:
                    print("The number of letters you have entered is too big. \n")    
                if len(guess) < 1:
                    print("The number of letters you have entered is too little. \n")
                guess = input("please input one letter.")
            if guessInLowerCase  in lettersGuessed:
                system('cls')
                print("Oops! You've already guessed that letter: ",getGuessedWord(secretWord, lettersGuessed))

            elif guessInLowerCase not in secretWord:
                system('cls')
                print("That letter is not in my word:",getGuessedWord(secretWord, lettersGuessed))
                chances-=1
            else:
                lettersGuessed.append(guessInLowerCase)
                system('cls')
                print("Nice guess: ",getGuessedWord(secretWord, lettersGuessed))
            lettersGuessed.append(guessInLowerCase)
        elif secretWord==getGuessedWord(secretWord, lettersGuessed):
            time.sleep(1)
            print("Congratulations, you won!")
            time.sleep(1)
            print("Thank you for playing, hope you enjoyed!")
            time.sleep(10)
            #the time.sleep function is so you can read it before cmd exits.
            break
    else:
            #here is the alternative, if you do not win the game.
            print("""
    __________
    |/       |
    |        |     
    |       (_)       
    |        |        
    |       /|\ 
    |       / \      
    |_____ /   \           
    """)
            print()
            time.sleep(1)
            print("Sorry, you ran out of guesses. The word was "+secretWord+".")
            time.sleep(1)
            print("Thank you for playing. Better luck next time!")
            time.sleep(10)
            #the time.sleep function is so you can read it before cmd exits. 

#the time and random imports are very important. Time lets me use the sleep command, which makes a line wait a certain amount of seconds before it moves onto the next line to execute.
#random is used as a choice, it selects a random choice, as im sure you figured out, from a given list/array of digits or strings. Here it gets a random string from my wordbank of
#secret words. This chosen word is now the secret word the user playing the game has to guess!!
import time
import random

#this is where the program actually begins!

secretWord= ["location", "destruction", "staged", "elementary", "responsibilities", "reinstated", "architecture", "pneumonia", "octagon", "psychopath", "happy", "looming", "substantial", "sorrow", "meandering", "mountainous"] 
hangman(random.choice(secretWord))
