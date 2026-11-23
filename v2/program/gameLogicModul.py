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
            hmi.clear()
            hmi.exitDisplay()
        case _:
            print("an error has occured")

def solo():
    #TODO
    print("sorry no solo game for now :/")
    input()

def duo():
    #TODO
    print("sorry no duo game for now :/")
    input()