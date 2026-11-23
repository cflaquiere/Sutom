from program import humanMachinInterfaceModul as hmi
from program import fileManagmentModul as fm
from program import gameLogicModul as gl

DICO_PATH = "./resource/dictionnary.txt"

if __name__ == "__main__":
    menuChoice : int = 0
    dictionnaryList : list[str] = []

    dictionnaryList = fm.readDictionnary(DICO_PATH)

    if( dictionnaryList != []):

        while(menuChoice != 5):
            hmi.clear()
            hmi.menuDisplay()
            menuChoice=hmi.menuInput()
            gl.dispacher(menuChoice,dictionnaryList)
    else:
        print(hmi.ANSI.RED+"the app integriti is compromised please ensure all files are present"+hmi.ANSI.RESET)