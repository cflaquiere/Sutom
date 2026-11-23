from random import randint
from program import humanMachinInterfaceModul as hmi
from program import verificationModul as verif

MAX_TRIES : int = 6

def dispacher(userChoice : int,dictionnaryList : list[str]):
    """relocate the user in fuction of its choice

    Args:
        userChoice (int): the choice of the user as a number
    """
    match userChoice:
        case 1:
            solo(dictionnaryList)
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

def difficultyHandler(dictionnaryList : list[str],difficulty : int):
    wordMinLen : int = 0
    wordMaxLen : int = 0
    difficultyList : list[str] = []

    match difficulty:
        case 1:
            wordMinLen = 2
            wordMaxLen = 6
        case 2:
            wordMinLen = 7
            wordMaxLen = 10
        case 3:
            wordMinLen = 11
            wordMaxLen = 15
        case 4:
            print("exiting...")
        case _:
            print(hmi.ANSI.RED + "a diffulty choice error occured" + hmi.ANSI.RESET)
    
    for word in dictionnaryList:
        if ((len(word) >= wordMinLen) and (len(word) <= wordMaxLen)):
            difficultyList.append(word)
    
    return difficultyList






def solo(dictionnaryList : list[str]):
    winToken : bool = False
    wordIndex : int = 0
    secretWord : str = ""
    difficulty : int = 0
    difficultyList : list[str] = []

    hmi.clear()
    hmi.difficultyMenuDisplay()
    difficulty = hmi.difficultyInput()
    if (difficulty != 4):
        difficultyList = difficultyHandler(dictionnaryList,difficulty)

        wordIndex = randint(0,len(difficultyList))
        secretWord = difficultyList[wordIndex]

        winToken = guessing(secretWord,1)


        if (winToken):
            print("congrats you won !")
        else:
            print("awwwn you lost :/")
        hmi.waitForUser()





def secretWordInput() -> str:
    """enable player one to choose the secret word

    Returns:
        str: the secret word in question
    """
    secretWord : str = ""

    hmi.clear()
    hmi.duoTitleDisplay()
    print("PLAYER ONE choose the word !")
    secretWord = input("enter the secret word : ")
    while (not verif.wordInputVerif(secretWord)):
        print(hmi.ANSI.RED+"please use only simple letters"+hmi.ANSI.RESET)
        secretWord = input("enter the secret word : ")
    return secretWord

def guessing(secretWord : str, mode : int) -> bool:
    """enable the player to guess the secret word

    Args:
        secretWord (str): the secret word witch need to be guessed

    Returns:
        bool: true if the player guessed else false
    """
    
    winToken : bool = False
    guessingWord : str = ""
    tries : int = 0
    validGuessToken : int = 0

    hmi.clear()
    if (mode == 1):
        hmi.soloTitleDisplay()
        print("guess the word !")
    else:
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
            validGuessToken = verif.guessInputVerif(secretWord,guessingWord) 
        winToken = verif.isAWin(secretWord,guessingWord)
        tries += 1
    
    return winToken


def duo():
    """the game cycle of gameplay with two players
    """
    secretWord : str = ""
    winToken : bool = False

    secretWord = secretWordInput()

    winToken = guessing(secretWord,2)

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