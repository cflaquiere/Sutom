import os

def fileExist(filePath : str) -> bool:
    """verify if a file exist

    Args:
        filePath (str): the path to the file

    Returns:
        bool: true if the file exist, false otherwise
    """
    return os.path.exists(filePath)

def difficultyInputVerif(userInput : str) -> bool:
    token : bool = False
    userDigit : int = 0

    if(userInput.isdecimal()):
        userDigit = int(userInput)

        if ((userDigit > 0) and (userDigit < 5)):
            token = True
    return token

def menuInputVerif(userInput : str) -> bool:
    """take the input from the user and return true of the input is correct

    Args:
        userInput (str): the user's input in default str format

    Returns:
        bool: token the boolean of verification
    """
    token : bool = False
    userDigit : int = 0

    if (userInput.isdecimal()):
            userDigit = int(userInput)

            if ((userDigit > 0) and (userDigit < 6)):
                token = True
    return token

def wordInputVerif(wordInput : str) -> bool:
    """verify if word is correctly input

    Args:
        wordInput (str): the word wich is needed to be verified

    Returns:
        bool: true if the word correctly input else false
    """
    token : bool = True
    wordInput = wordInput.upper()
    for letter in wordInput:
        if ((letter < "A" ) or (letter > "Z" )):
            token = False
    
    return token


def guessInputVerif(secretWord : str,guessingWord : str) -> int:
    """verify if the guessing Word is correctly input

    Args:
        secretWord (str): the word to guess
        guessingWord (str): the word trying to guess

    Returns:
        int: 0, everything is right, 1 , size problem, 2 , begining problem , 3, characters problem
    """
    token : int = 0
    if (len(secretWord) != len(guessingWord)):
        token = 1
    elif(secretWord[0] != guessingWord[0]):
        token = 2
    elif(not wordInputVerif(guessingWord)):
        token = 3
    return token

def isAWin(secretWord : str, guessingWord : str) -> bool:
    """return if the secret word is the same as the guess

    Args:
        secretWord (str): the word which need to be guessed
        guessingWord (str): the word which is trying to guess

    Returns:
        bool: true if every letters are the same else false
    """
    return secretWord == guessingWord

def wellPlacedLetter(secretWord : str,guessingLetter : str,letterIndex : int) -> bool:
    """return if the letter is well placed

    Args:
        secretWord (str): the word wich need to be guessed
        guessingLetter (str): the letter trying to be guessed
        letterIndex (int): the place of the letter in the word

    Returns:
        bool: true if the letter is at its right place, else false
    """

    return secretWord[letterIndex] == guessingLetter