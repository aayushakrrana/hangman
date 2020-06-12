import random

def load_words():
    WORDLIST_FILENAME = "C:\\Users\\AAYUSH_RANA\\Documents\\GitHub\\hangman\\words.txt"
    word_list=[]
    f=open(WORDLIST_FILENAME,"r")
    line = f.readline()
    word_list = line.split()
    return (word_list)

def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
