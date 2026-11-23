import os
from program import verificationModul as verif

def clear():
    """use the clear system from terminal within all operating systems
    """
    if ( os.name == "nt" ):
        os.system("cls")
    else:
        os.system("clear")


def titleDisplay():
    """display the title of the game
    """
    print()
    print("▄█████ ██  ██ ██████ ▄████▄ ██▄  ▄██ ")
    print("▀▀▀▄▄▄ ██  ██   ██   ██  ██ ██ ▀▀ ██ ")
    print("█████▀ ▀████▀   ██   ▀████▀ ██    ██ ")
    print()

def menuDisplay():
    """display the game's menu
    """
    titleDisplay()
    print("----------------------")
    print(" 1 - solo")
    print(" 2 - duo")
    print(" 3 - display scores")
    print(" 4 - display rules")
    print(" 5 - quit")
    print("----------------------")


def menuInput() -> int:
    """return the correct user input for the menu
    Returns:
        int: the number corresponding to the menu's choice
    """

    userInput : str = ""

    userInput = input("enter a choice : ")
    while(not verif.menuInputVerif(userInput)):
        print("user choice error")
        userInput = input("enter a choice : ")
    
    return int(userInput)


def scoresDisplay():
    #TODO
    print("sorry no scores available for now :/")

def rulesDisplay():
    #TODO
    print("no rules to display for now :/")