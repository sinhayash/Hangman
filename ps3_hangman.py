# Author Yash Sinha
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string


WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
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
    # FILL IN YOUR CODE HERE...
    String = ''
    for index, value in enumerate(lettersGuessed):
        String += value
    for char in secretWord:
        boolean = char in String
        if(boolean == False):
            return False
    return True     


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    PrintedString = ''
    String = ''
    for index, value in enumerate(lettersGuessed):
        String += value
    for char in secretWord:
        if(char in String):
            PrintedString += char
        else:
            PrintedString += '_ '
    return PrintedString


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    String = ''
    PrintedString = ''
    for index, value in enumerate(lettersGuessed):
        String += value
    String.lower()
    TestString = 'abcdefghijklmnopqrstuvwxyz'
    for char in TestString:
        if(not(char in String)):
           PrintedString += char
    return PrintedString.lower()

#def mistakesMade(secretWord, guess, lettersGuessed):
#    String = ''
#    for index, value in enumerate(lettersGuessed):
#        String += value
#    if (not(guess in String)):
#        guessMade += 1

def makeGuess(lettersGuessed, guessMade):
    print('You have '+str((8-guessMade))+' guesses left,')
    print('Available letters: '+getAvailableLetters(lettersGuessed))
    guess = raw_input('Please guess a letter: ').lower()
    return guess
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    guessMade = 0
    lettersGuessed = []
    guessTemp = []
    String = ''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    while(guessMade<8):
        print('------------')
        guess = makeGuess(lettersGuessed, guessMade)
        for index, value in enumerate(lettersGuessed):
            String += value
        lettersGuessed += guess
        if(guess in String):
            print('Oops! You\'ve already guessed that letter: '+getGuessedWord(secretWord, lettersGuessed))
            
        if(not(guess in String)):
            if(not(guess in secretWord)):
                print('Oops! That letter is not in my word: '+getGuessedWord(secretWord, lettersGuessed))
                guessMade+=1
            elif(guess in secretWord):
                print('Good guess: '+getGuessedWord(secretWord, lettersGuessed))
                if(secretWord==getGuessedWord(secretWord, lettersGuessed+[guess])):
                    print('------------')
                    print('Congratulations, you won!')
                    break
    if(not(secretWord==getGuessedWord(secretWord, lettersGuessed+[guess]))):
        print('------------')
        print('Sorry, you ran out of guesses. The word was '+secretWord)
    

   # print('You have '+(8-guessMade)+' guesses left,')
   # char guess = raw_input('Please guess a letter: ').lower()
   # mistakesMade(secretWord, guess, lettersGuessed)
    





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
