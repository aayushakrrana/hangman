import string
from words import choose_word
from images import IMAGES
import re
import sys
import random

def is_word_guessed(secret_word, letters_guessed):
    a=set(secret_word)
    b=set(letters_guessed)
    if(a==b):
        print(" * * Congratulations, you won! * * ", end='\n\n')
        sys.exit()
        


def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word

def get_available_letters(letters_guessed):
    letters_left = (string.ascii_lowercase)
    letters_left = (set(letters_guessed)^set(letters_left))
    letters_left =(sorted(letters_left))
    letters_left = ''.join(letters_left)
    return(letters_left)

def ifValid(letter,available_letters,secret_word, letters_guessed,prev_hint):
    if (letter=='hint'):
        return True
    if (len(letter)>1):
            print ("Error! Only 1 characters allowed!")
            return False 
    elif not re.match("^[a-z]*$", letter):
        print ("Error! Only letters a-z allowed!")
        return False
    elif letter not in available_letters:
        print("")
        print("Word already guessed!!!: {} ".format(get_guessed_word(secret_word, letters_guessed)))
        print("")
        return False
    else:
        return True

def hint(secret_word,letters_guessed):
    letters_left = (set(secret_word)^set(letters_guessed))
    return(random.sample(letters_left, 1))
    
    

def hangman(secret_word):
    print("")
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is {} letters long.".format(
        str(len(secret_word))), end='\n\n')

    letters_guessed = []
    print(secret_word)
    prev_hint=False
    available_lives=0
    while(1):
        available_letters = get_available_letters(letters_guessed)
        print("Available letters: {}                 ".format(available_letters),end="")
        print("Remaining lives : ", end="" )
        print(8-available_lives)
        print("")
        guess = input("Please guess a letter: ")
        letter = guess.lower()
                    
        if ifValid(letter,available_letters,secret_word, letters_guessed,prev_hint)==True:
            if letter in secret_word :
                letters_guessed.append(letter)
                print("Good guess: {} ".format(
                    get_guessed_word(secret_word, letters_guessed)))
                is_word_guessed(secret_word, letters_guessed)
                print("")
            elif letter=="hint":
                if prev_hint==False:
                    print("HINT : -{}-".format(hint(secret_word,letters_guessed)))
                    prev_hint=True
                else:
                    print("**** Hint already used!! ****")    
            else:
                print(IMAGES[available_lives])
                available_lives=available_lives+1
                print("")
                print("Oops! That letter is not in my word: {} ".format(
                get_guessed_word(secret_word, letters_guessed)))
                letters_guessed.append(letter)
                print("")
                is_word_guessed(secret_word, letters_guessed)
                if(available_lives>7):
                    print("****Game Over****")
                    sys.exit()
                print("")
        else:
            continue
            
            
  


# Load the list of words into the variable wordlist
# So that it can be accessed from anywhere in the program
secret_word = choose_word()
hangman(secret_word)
