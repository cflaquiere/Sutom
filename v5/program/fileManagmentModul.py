from program import verificationModul as verif
from program import humanMachinInterfaceModul as hmi
import pickle
from typing import BinaryIO

class Register:
        difficulty : int
        score : int

def readDictionnary(dicoPath : str) -> list[str]:
    """read the dictionnary file and output its content as a list

    Args:
        dicoPath (str): the path to the dictionnary

    Returns:
        list[str]: the list content of the dictionnary
    """
    
    dictionnaryList : list[str] = []

    print("loading the dictionnary  ...")

    if verif.fileExist(dicoPath):
        with open(dicoPath, "r") as file:
            for line in file.readlines():
                dictionnaryList.append(line.replace("\n",""))
    else:
        print(hmi.ANSI.RED+"the dictionnary is not found"+hmi.ANSI.RESET)

    print("dictionnary loaded ! ")

    return dictionnaryList

def writeScore(scorePath : str,difficulty : int, score : int):
    """enable to sort and write the score in file using binary file managment

    Args:
        scorePath (str): the path to the score
        difficulty (int): the difficulty choosed by the user
        score (int): the score of the user
    """

    file : BinaryIO
    register : Register = Register()
    register.difficulty = difficulty
    register.score = score

    load : list[Register] = []
    sortedList : list[Register] = []
    
    load = readScore(scorePath)

    load.append(register)

    sortedList = bubbleSort(load)

    file = open(scorePath,"wb")
    pickle.dump(sortedList,file)
    #fermeture du fichier
    file.close()

def bubbleSort(registerList : list[Register])-> list[Register]:
    """a sorting function using bubble sort algorithme

    Args:
        registerList (list[Register]): the list of all the scores registered with their difficulties

    Returns:
        list[Register]: the registers scores with difficulty in order
    """

    length : int = 0
    
    length = len(registerList)

    for i in range(length):
        for j in range(0, length - i - 1):
            if registerList[j].score < registerList[j + 1].score:
                # Échange les éléments
                registerList[j], registerList[j + 1] = registerList[j + 1], registerList[j]
    
    return registerList
    
    

    
def readScore(scorePath : str) -> list[Register]:
    """enable to read the content of the score file

    Args:
        scorePath (str): the path to the score file

    Returns:
        list[Register]: the list of scores and difficulty registered
    """
    file : BinaryIO
    endFile : bool = False
    registerList : list[Register] = []

    if verif.fileExist(scorePath):
        file = open(scorePath,"rb")
        while (not endFile):
            try :
                registerList = pickle.load(file)
            except EOFError:
                endFile = True
    return registerList

def readScoreDisplay(scorePath : str) -> list[list[int]]:
    """transform the registers list in a list of int list

    Args:
        scorePath (str): the path to the score file

    Returns:
        list[list[int]]: a list of list of int corresponding to the difficulty and the score registered
    """
    load : list[Register] = []
    registerList : list[list[int]] = []

    load = readScore(scorePath)

    for register in load:
        registerList.append([register.difficulty,register.score])
    
    return registerList