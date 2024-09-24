import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    c = 0
    for i in lettersGuessed:
        if i in secretWord:
            c += 1
    return c == len(secretWord)

def getGuessedWord(secretWord, lettersGuessed):
    s = []
    for i in secretWord:
        if i in lettersGuessed:
            s.append(i)
    ans = ''
    for i in secretWord:
        if i in s:
            ans += i
        else:
            ans += '_ '
    return ans

def getAvailableLetters(lettersGuessed):
    import string
    ans = list(string.ascii_lowercase)
    for i in lettersGuessed:
        ans.remove(i)
    return ''.join(ans)

def printHangman(mistakes):
    hangman_pics = [
        """
          ------
          |    |
          |
          |
          |
          |
        __|__
        """,
        """
          ------
          |    |
          |    O
          |
          |
          |
        __|__
        """,
        """
          ------
          |    |
          |    O
          |    |
          |
          |
        __|__
        """,
        """
          ------
          |    |
          |    O
          |   /|
          |
          |
        __|__
        """,
        """
          ------
          |    |
          |    O
          |   /|\\
          |
          |
        __|__
        """,
        """
          ------
          |    |
          |    O
          |   /|\\
          |   /
          |
        __|__
        """,
        """
          ------
          |    |
          |    O
          |   /|\\
          |   / \\
          |
        __|__
        """
    ]
    print(hangman_pics[mistakes])

def hangman(secretWord):
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is", len(secretWord), "letters long.")

    global lettersGuessed
    mistakeMade = 0
    lettersGuessed = []

    while 6 - mistakeMade > 0:
        if isWordGuessed(secretWord, lettersGuessed):
            print("-------------")
            print("Congratulations, you won!")
            break
        else:
            print("-------------")
            print("You have", 6 - mistakeMade, "guesses left.")
            print("Available letters:", getAvailableLetters(lettersGuessed))
            guess = str(input("Please guess a letter: ")).lower()

            if guess in lettersGuessed:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))

            elif guess in secretWord and guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print("Good guess:", getGuessedWord(secretWord, lettersGuessed))

            else:
                lettersGuessed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:", getGuessedWord(secretWord, lettersGuessed))
                printHangman(mistakeMade)  # Print hangman drawing

        if 6 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was:", secretWord)
            printHangman(6)  # Print final hangman state
            break
        else:
            continue

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
