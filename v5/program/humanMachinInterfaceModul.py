import os
from program import verificationModul as verif
from program import fileManagmentModul as fm

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
        #windows clear
        os.system("cls")
    else:
        #linux and mac clear
        os.system("clear")

def separator():
    """display a green separator
    """
    print(ANSI.GREEN+"----------------------"+ANSI.RESET)

def gameOverDisplay():
    """display the message for when the user lost
    """
    print(ANSI.RED)
    print(" ▄████  ▄████▄ ██▄  ▄██ ██████   ▄████▄ ██  ██ ██████ █████▄  ")
    print("██  ▄▄▄ ██▄▄██ ██ ▀▀ ██ ██▄▄     ██  ██ ██▄▄██ ██▄▄   ██▄▄██▄ ")
    print(" ▀███▀  ██  ██ ██    ██ ██▄▄▄▄   ▀████▀  ▀██▀  ██▄▄▄▄ ██   ██ ")
    print(ANSI.RESET)

def winDisplay():
    """display the message for when the user win
    """
    print(ANSI.GREEN)
    print("██ ██████ ▄█████   ▄████▄   ██     ██ ██ ███  ██ ")
    print("██   ██   ▀▀▀▄▄▄   ██▄▄██   ██ ▄█▄ ██ ██ ██ ▀▄██ ")
    print("██   ██   █████▀   ██  ██    ▀██▀██▀  ██ ██   ██ ")
    print(ANSI.RESET)
                                                                                                   

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
    """display the title of the duo game
    """
    print(ANSI.BLUE)               
    print("                                                      ")
    print("████▄  ██  ██ ▄████▄    ▄████  ▄████▄ ██▄  ▄██ ██████ ")
    print("██  ██ ██  ██ ██  ██   ██  ▄▄▄ ██▄▄██ ██ ▀▀ ██ ██▄▄   ")
    print("████▀  ▀████▀ ▀████▀    ▀███▀  ██  ██ ██    ██ ██▄▄▄▄ ")
    print("                                                      ")
    print(ANSI.RESET)

def soloTitleDisplay():
    """display the title of the solo game
    """
    print(ANSI.BLUE)
    print("                                                             ")
    print("▄█████ ▄████▄ ██     ▄████▄    ▄████  ▄████▄ ██▄  ▄██ ██████ ")
    print("▀▀▀▄▄▄ ██  ██ ██     ██  ██   ██  ▄▄▄ ██▄▄██ ██ ▀▀ ██ ██▄▄   ")
    print("█████▀ ▀████▀ ██████ ▀████▀    ▀███▀  ██  ██ ██    ██ ██▄▄▄▄ ")
    print(ANSI.RESET)

def scoreTitleDisplay():
    """display the title of the scores
    """
    print(ANSI.BLUE)
    print(" ▄▄▄▄  ▄▄▄▄  ▄▄▄  ▄▄▄▄  ▄▄▄▄▄ ")
    print("███▄▄ ██▀▀▀ ██▀██ ██▄█▄ ██▄▄  ")
    print("▄▄██▀ ▀████ ▀███▀ ██ ██ ██▄▄▄ ")
    print(ANSI.RESET)
                                                                             

def titleDisplay():
    """display the title of the game
    """
    print(ANSI.BLUE)
    print("▄█████ ██  ██ ██████ ▄████▄ ██▄  ▄██ ")
    print("▀▀▀▄▄▄ ██  ██   ██   ██  ██ ██ ▀▀ ██ ")
    print("█████▀ ▀████▀   ██   ▀████▀ ██    ██ ")
    print(ANSI.RESET)

def difficultyTitleDisplay():
    """display the title of difficulties menu
    """
    print(ANSI.BLUE)
    print("                                                             ")
    print("████▄  ██ ██████ ██████ ██ ▄█████ ██  ██ ██    ██████ ██  ██ ")
    print("██  ██ ██ ██▄▄   ██▄▄   ██ ██     ██  ██ ██      ██    ▀██▀  ")
    print("████▀  ██ ██     ██     ██ ▀█████ ▀████▀ ██████  ██     ██   ")
    print(ANSI.RESET)
                                                             

def rulesTitleDisplay():
    """display the title of the rules
    """

    print(ANSI.BLUE)                        
    print("                                    ")
    print("█████▄  ██  ██ ██     ██████ ▄█████ ")
    print("██▄▄██▄ ██  ██ ██     ██▄▄   ▀▀▀▄▄▄ ")
    print("██   ██ ▀████▀ ██████ ██▄▄▄▄ █████▀ ")
    print(ANSI.RESET)
                                    

def rulesDisplay():
    """display the rules with colors
    """
    clear()
    rulesTitleDisplay()
    separator()
    print("The principle of the game is simple.")
    print("A mystery word consisting of between 2 and 15 letters must be guessed in a")
    print("maximum of six attempts.")
    separator()
    print("To do this, two rules must be followed:")
    print("• Suggest a word beginning with the starting letter.")
    print("• Suggest a word of the required length.")
    separator()
    print("With each attempt, clues are given in the form of colours:")
    print("• Letters in the correct position appear in" + ANSI.RED + " red." + ANSI.RESET)
    print("• Letters present in the word but in the wrong position are shown in" + ANSI.YELLOW + " yellow." + ANSI.RESET)
    print("• Letters not present in the word remain uncoloured.")
    print()
    waitForUser()


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

def difficultyMenuDisplay():
    """display the diffuclty's menu
    """
    difficultyTitleDisplay()
    separator()
    print(" 1 - easy Level ( 2-6 letters)")
    print(" 2 - medium Level (7-10 letters)")
    print(" 3 - hard Level ( 11-15 letters)")
    print(" 4 - return to main Menu")
    separator()

def displayColoredHint(colorList : list[str],guessingWord : str):
    """display the hints with colors

    Args:
        colorList (list[str]): the list of colors in corelation to the secret word
        guessingWord (str): the input of the user
    """
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

def difficultyInput() -> int:
    """enable the user to input the difficulty it wants

    Returns:
        int: the integer corresponding to this difficulty
    """

    userInput : str = ""

    userInput = input("enter a choice : ")
    while(not verif.difficultyInputVerif(userInput)):
        print(ANSI.RED+"user choice error"+ANSI.RESET)
        userInput = input("enter a choice : ")
    
    return int(userInput)



def scoresDisplay(scorePath : str):
    """enable the user to see the scores

    Args:
        scorePath (str): the path to the score file
    """
    registers : list[list[int]]
    easyDifficulty : list[int] = []
    mediumDifficulty : list[int] = []
    hardDifficulty : list[int] = []

    #reading of all scores
    registers = fm.readScoreDisplay(scorePath)

    #sorting scores by difficulties
    for register in registers:
        if (register[0] == 1):
            easyDifficulty.append(register[1])
        elif (register[0] == 2):
            mediumDifficulty.append(register[1])
        elif(register[0] == 3):
            hardDifficulty.append(register[1])
        else:
            print("difficulty unknown")
    
    #display
    clear() 
    scoreTitleDisplay()   
    print(ANSI.BLUE + "HARD LEVEL : " + ANSI.RESET)
    separator()
    displayDifficultyList(hardDifficulty)
    separator()
    print(ANSI.BLUE + "MEDIUM LEVEL : " + ANSI.RESET)
    separator()
    displayDifficultyList(mediumDifficulty)
    separator()
    print(ANSI.BLUE + "EASY LEVEL : " + ANSI.RESET)
    separator()
    displayDifficultyList(easyDifficulty)
    separator()
    waitForUser()
        
def displayDifficultyList(difficultyList : list[int]):
    """display the scores corresponding to the difficulty

    Args:
        difficultyList (list[int]): the list of scores witch need to be displayed
    """

    for difficulty in difficultyList :
        print(difficulty)

