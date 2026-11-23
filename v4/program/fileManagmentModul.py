from program import verificationModul as verif
from program import humanMachinInterfaceModul as hmi

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