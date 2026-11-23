import os
from program import verificationModul as verif

class ANSI:
    RESET = "\033[0m"

    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"


def clear():
    """use the clear system from terminal within all operating systems
    """
    if ( os.name == "nt" ):
        os.system("cls")
    else:
        os.system("clear")

def separator():
    """display a green separator
    """
    print(ANSI.GREEN+"----------------------"+ANSI.RESET)

def exitDisplay():
    """display the message of exit
    """
    print(ANSI.BLUE)              
    print("                      ▄▄ ")
    print("█████▄ ██  ██ ██████  ██ ")
    print("██▄▄██  ▀██▀  ██▄▄    ██ ")
    print("██▄▄█▀   ██   ██▄▄▄▄  ▄▄ ")
    print(ANSI.RESET)

def duoTitleDisplay():
    print(ANSI.BLUE)               
    print("                                                      ")
    print("████▄  ██  ██ ▄████▄    ▄████  ▄████▄ ██▄  ▄██ ██████ ")
    print("██  ██ ██  ██ ██  ██   ██  ▄▄▄ ██▄▄██ ██ ▀▀ ██ ██▄▄   ")
    print("████▀  ▀████▀ ▀████▀    ▀███▀  ██  ██ ██    ██ ██▄▄▄▄ ")
    print("                                                      ")
    print(ANSI.RESET)

def titleDisplay():
    """display the title of the game
    """
    print(ANSI.BLUE)
    print("▄█████ ██  ██ ██████ ▄████▄ ██▄  ▄██ ")
    print("▀▀▀▄▄▄ ██  ██   ██   ██  ██ ██ ▀▀ ██ ")
    print("█████▀ ▀████▀   ██   ▀████▀ ██    ██ ")
    print(ANSI.RESET)

def menuDisplay():
    """display the game's menu
    """
    titleDisplay()
    separator()
    print(" 1 - solo")
    print(" 2 - duo")
    print(" 3 - display scores")
    print(" 4 - display rules")
    print(" 5 - quit")
    separator()

def displayColoredHint(colorList : list[str],guessingWord : str):
    coloredLetter : str = ""

    for lettersNumber in range(len(colorList)):
            coloredLetter = colorList[lettersNumber]
            match coloredLetter:
                case 'w':
                    print(guessingWord[lettersNumber]+" ",end="")
                case 'r':
                    print(ANSI.RED + guessingWord[lettersNumber] + ANSI.RESET + " ",end="")
                case 'y':
                    print(ANSI.YELLOW + guessingWord[lettersNumber] + ANSI.RESET + " ",end="")
                case _:
                    print()
                    print(ANSI.RED + "error on colors" + ANSI.RESET)
    print()

def waitForUser():
    """wait for the user to aknwoledge a message
    """
    input("press enter to continue : ")

def guessErrorsPrints(validGuessToken : int):
    """display an error in function of the value of validGuessToken

    Args:
        validGuessToken (int): the error value of the guessInputVerif function
    """
    match validGuessToken:
        case 1:
            print("the size do not correspond retry")
        case 2:
            print("the guess do not begin with the same letter retry")
        case 3:
            print("no special characters allowed retry")
        case _:
            print(ANSI.RED+"an error occured" + ANSI.RESET)


def menuInput() -> int:
    """return the correct user input for the menu
    Returns:
        int: the number corresponding to the menu's choice
    """

    userInput : str = ""

    userInput = input("enter a choice : ")
    while(not verif.menuInputVerif(userInput)):
        print(ANSI.RED+"user choice error"+ANSI.RESET)
        userInput = input("enter a choice : ")
    
    return int(userInput)


def scoresDisplay():
    #TODO
    print("sorry no scores available for now :/")
    input()

def rulesDisplay():
    #TODO
    print("no rules to display for now :/")
    input()