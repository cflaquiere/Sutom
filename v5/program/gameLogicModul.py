from random import randint
from program import humanMachinInterfaceModul as hmi
from program import verificationModul as verif
from program import fileManagmentModul as fm

MAX_TRIES : int = 6
SCORE_PATH : str = "./files/scores.dat"



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
            hmi.scoresDisplay(SCORE_PATH)
        case 4:
            hmi.rulesDisplay()
        case 5:
            hmi.clear()
            hmi.exitDisplay()
        case _:
            print("an error has occured")

def scoreCalcul(difficulty : int,tries : int) -> int:
    """calculate score in function of difficulty and number of tries

    Args:
        difficulty (int): the difficulty choosed
        tries (int): the number of tries needed to guess the secret word

    Returns:
        int: the total score of the player
    """
    score : int = 0
    base : int = difficulty * 10
    
    if (tries == 0):
        #perfect score case
        score = base + 5
    else:
        score = base - (tries * 2) + 2
    
    return score
        

def difficultyHandler(dictionnaryList : list[str],difficulty : int) -> list[str]:
    """handle the difficulty in order to output the corresponding list of words

    Args:
        dictionnaryList (list[str]): the words of the dictionnary
        difficulty (int): the emount of difficulty

    Returns:
        list[str]: the list of words corresponding to the difficulty
    """
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
    """the game cycle of gameplay with one player

    Args:
        dictionnaryList (list[str]): all the words of the dictionnary
    """
    triesNumber : int = 0
    wordIndex : int = 0
    secretWord : str = ""
    difficulty : int = 0
    difficultyList : list[str] = []
    score : int = 0

    hmi.clear()
    hmi.difficultyMenuDisplay()
    difficulty = hmi.difficultyInput()
    if (difficulty != 4):
        difficultyList = difficultyHandler(dictionnaryList,difficulty)

        wordIndex = randint(0,len(difficultyList))
        secretWord = difficultyList[wordIndex]

        triesNumber = guessing(secretWord,1)

        score = scoreCalcul(difficulty,triesNumber)

        endOfGame(triesNumber,secretWord,score)
        
        fm.writeScore(SCORE_PATH,difficulty,score)
        
        hmi.waitForUser()

def endOfGame(triesNumber : int,secretWord : str,score : int):
    """manage the end of game scenarios

    Args:
        triesNumber (int): the number of tries
        secretWord (str): the word to guess
        score (int): the actual score of the player
    """

    if (triesNumber < MAX_TRIES):
            hmi.clear()
            hmi.winDisplay()
            print("congrats you won !")
            print("your score is : " + str(score))
            print("word was : " + secretWord)
    else:
        hmi.clear()
        hmi.gameOverDisplay()
        print("awwwn you lost :/")
        print("the word was : " + secretWord)



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
    while ((not verif.wordInputVerif(secretWord)) and (len(secretWord) >= 2)):
        print(hmi.ANSI.RED+"please use only simple letters"+hmi.ANSI.RESET)
        secretWord = input("enter the secret word : ")
    return secretWord

def guessing(secretWord : str, mode : int) -> int:
    """enable the player to guess the secret word

    Args:
        secretWord (str): the secret word witch need to be guessed

    Returns:
        bool: true if the player guessed else false
    """
    
    winToken : bool = False
    guessingWord : str = ""
    tries : int = -1
    validGuessToken : int = 0

    hmi.clear()
    if (mode == 1):
        hmi.soloTitleDisplay()
        print("guess the word !")
    else:
        hmi.duoTitleDisplay()
        print("PLAYER TWO guess the word !")
    while((tries < MAX_TRIES) and (not winToken)):
        tries += 1
        print(f"try number : {tries}")
        hint(secretWord,guessingWord)
        guessingWord = input("enter the guess : ")
        validGuessToken = verif.guessInputVerif(secretWord,guessingWord)
        while(validGuessToken != 0):
            hmi.guessErrorsPrints(validGuessToken)
            guessingWord = input("enter the guess : ")
            validGuessToken = verif.guessInputVerif(secretWord,guessingWord) 
        winToken = verif.isAWin(secretWord,guessingWord)
    
    return tries

def getDuoDifficulty(secretWord : str) -> int:
    """enable to output the current difficulty of the duo mode

    Args:
        secretWord (str): the secret word enterd by the first pllayer

    Returns:
        int: the difficulty of the word
    """
    secretLen : int = len(secretWord)
    difficulty : int = 0

    if(secretLen < 2):
        difficulty = 0
    elif ((secretLen >= 2) and (secretLen <= 6)):
        difficulty = 1
    elif((secretLen >= 7) and (secretLen <= 10)):
        difficulty = 2
    else:
        difficulty = 3
    
    return difficulty


def duo():
    """the game cycle of gameplay with two players
    """
    secretWord : str = ""
    tries : int = 0
    difficulty : int = 0
    score : int = 0

    secretWord = secretWordInput()

    difficulty = getDuoDifficulty(secretWord)

    tries = guessing(secretWord,2)

    score = scoreCalcul(difficulty,tries)

    endOfGame(tries,secretWord,score)

    fm.writeScore(SCORE_PATH,difficulty,score)

    hmi.waitForUser()
    

def colorsInitialisation(secretWord : str) -> list[str]:
    """return an array of "w" corresponding the word to guess

    Args:
        secretWord (str): the word to guess

    Returns:
        list[str]: the list of "w"
    """
    return ["w"]*len(secretWord)

def initialGuessDisplay(secretList : list[str]):
    """display the first hint to find the secret word

    Args:
        secretList (list[str]): the secret word in the shape of a list
    """
    lettersNumber : int = 0
    
    print(hmi.ANSI.RED+secretList[0]+hmi.ANSI.RESET,end="")
    for lettersNumber in range(len(secretList)-1):
        print(" _ ",end="")
    print(f"( {lettersNumber+1}, letters )")


def hint(secretWord : str, guessingWord : str ):
    """build the second hint using the guess of the user

    Args:
        secretWord (str): the word to guess
        guessingWord (str): the guess of the user
    """

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