from program import humanMachinInterfaceModul as hmi
from program import verificationModul as verif

MAX_TRIES : int = 6

def dispacher(userChoice : int):
    """relocate the user in fuction of its choice

    Args:
        userChoice (int): the choice of the user as a number
    """
    match userChoice:
        case 1:
            solo()
        case 2:
            duo()
        case 3:
            hmi.scoresDisplay()
        case 4:
            hmi.rulesDisplay()
        case 5:
            hmi.clear()
            hmi.exitDisplay()
        case _:
            print("an error has occured")


def solo():
    #TODO
    print("sorry no solo game for now :/")
    input()

def secretWordInput() -> str:
    """enable player one to choose the secret word

    Returns:
        str: the secret word in question
    """
    hmi.clear()
    hmi.duoTitleDisplay()
    print("PLAYER ONE choose the word !")
    secretWord = input("enter the secret word : ")
    while (not verif.wordInputVerif(secretWord)):
        print(hmi.ANSI.RED+"please use only simple letters"+hmi.ANSI.RESET)
        secretWord = input("enter the secret word (no special characters) : ")
    return secretWord

def guessing(secretWord : str) -> bool:
    
    winToken : bool = False
    guessingWord : str = ""
    tries : int = 0
    validGuessToken : int = 0

    hmi.clear()
    hmi.duoTitleDisplay()
    print("PLAYER TWO guess the word !")
    while((tries <= MAX_TRIES) and (not winToken)):
        print(f"try number : {tries}")
        hint(secretWord,guessingWord)
        guessingWord = input("enter the guess : ")
        validGuessToken = verif.guessInputVerif(secretWord,guessingWord)
        while(validGuessToken != 0):
            hmi.guessErrorsPrints(validGuessToken)
            guessingWord = input("enter the guess : ")       
        winToken = verif.isAWin(secretWord,guessingWord)
        tries += 1
    
    return winToken


def duo():
    """the game cycle of gameplay with two players
    """
    secretWord : str = ""
    winToken : bool = False

    secretWord = secretWordInput()

    winToken = guessing(secretWord)

    if (winToken):
        print("congrats you won !")
    else:
        print("awwwn you lost :/")
    hmi.waitForUser()
    

def colorsInitialisation(secretWord : str) -> list[str]:
    return ["w"]*len(secretWord)

def initialGuessDisplay(secretList : list[str]):
    lettersNumber : int = 0
    
    print(hmi.ANSI.RED+secretList[0]+hmi.ANSI.RESET,end="")
    for lettersNumber in range(len(secretList)-1):
        print(" _ ",end="")
    print(f"( {lettersNumber+1}, letters )")


def hint(secretWord : str, guessingWord : str ):

    lettersNumber : int = 0
    letterToRemove : str = ""
    listNumber : int = 0
    secretList : list[str] = list(secretWord)
    guessList : list[str] = list(guessingWord)
    colorList : list[str] = []

    if (guessingWord == ""):
        initialGuessDisplay(secretList)

    else:

        colorList = colorsInitialisation(secretWord)

        for lettersNumber in range(len(colorList)):
            if(verif.wellPlacedLetter(secretWord,guessingWord[lettersNumber],lettersNumber)):
                colorList[lettersNumber] = "r"
                guessList.pop(listNumber)
                secretList.pop(listNumber)
            else:
                listNumber += 1

        listNumber = 0

        for lettersNumber in range(len(colorList)):
            if colorList[lettersNumber] != "r":
                if(guessList[listNumber] in secretList):  
                    colorList[lettersNumber] = "y"
                    letterToRemove = guessList[listNumber]
                    guessList.remove(letterToRemove)
                    secretList.remove(letterToRemove)
                else:
                    listNumber += 1
        

        hmi.displayColoredHint(colorList,guessingWord)