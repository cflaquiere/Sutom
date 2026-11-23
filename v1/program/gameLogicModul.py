from program import humanMachinInterfaceModul as hmi


def dispacher(userChoice : int):
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
            print("exiting...")
        case _:
            print("an error has occured")

def solo():
    #TODO
    print("solo game")

def duo():
    #TODO
    print("duo game")