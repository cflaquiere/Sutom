
def menuInputVerif(userInput : str) -> bool:
    """take the input from the user and return true of the input is correct

    Args:
        userInput (str): the user's input in default str format

    Returns:
        bool: token the boolean of verification
    """
    token : bool = False
    if (userInput.isdecimal()):
            userDigit = int(userInput)

            if ((userDigit > 0) and (userDigit < 6)):
                token = True
    return token
            