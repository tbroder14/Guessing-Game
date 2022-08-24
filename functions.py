from time import sleep

def playerGuessText(attempts):

    sleep(0.75)
    playerGuess = int(input(f"Pick any number between 1 and 100. You have {attempts} attempts remaining." + "\n"))
    return playerGuess


def attemptUpdater(attempts, number):
    return attempts + number