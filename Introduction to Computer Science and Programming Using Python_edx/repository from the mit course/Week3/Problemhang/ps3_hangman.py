# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/jmstf/Documents/Python Scripts/Week3/Problemhang/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for x in secretWord:
         if x not in lettersGuessed:
             return False
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    final=[]
    for x in range(len(secretWord)):
        if secretWord[x] in lettersGuessed:
           final.extend(secretWord[x])
        else:
           final.extend('_')
    p=''
    for x in range(len(final)):
        if final[x]=='_':
           p=p+'_ '
        else:
           p=p+final[x]
    return p


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    s=string.ascii_lowercase
    p=''
    for x in s:
        if x not in lettersGuessed:
           p=p+x
    return p

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print("Welcome to the game, Hangman!")
    secretWord=chooseWord(wordlist)
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    print("------------")
    lettersGuessed=[]
    mistakesMade=0
    for x in range(8,0,-1):
        print("You have ",x," guesses left.")
        print("Available letters:",getAvailableLetters(lettersGuessed))
        availableLetters=getAvailableLetters(lettersGuessed)
        l=input("Please guess a letter:")
        if l in lettersGuessed:
            print("Oops! You 've already guessed that letter:",getGuessedWord(secretWord,lettersGuessed))
            x+=1
        else:
            if l in secretWord:
                lettersGuessed.extend(l)
                print("Good guess:",getGuessedWord(secretWord,lettersGuessed))
            else:
                lettersGuessed.extend(l)
                print('Oops! That letter is not in my word:',getGuessedWord(secretWord,lettersGuessed))
                mistakesMade+=1
        if isWordGuessed(secretWord,lettersGuessed)==True:
            break
    if isWordGuessed(secretWord,lettersGuessed)==True:
        print("Congratulations, you won!")
    else:
        print("Sorry, you ran out of guesses. The word was:",secretWord)
        
    
secretWord = chooseWord(wordlist).lower()
hangman(secretWord)