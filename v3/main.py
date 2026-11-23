from program import humanMachinInterfaceModul as hmi
from program import gameLogicModul as gl

if __name__ == "__main__":
    menuChoice : int = 0
    while(menuChoice != 5):
        hmi.clear()
        hmi.menuDisplay()
        menuChoice=hmi.menuInput()
        gl.dispacher(menuChoice)