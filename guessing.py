import random
from time import sleep
from functions import *

# winnerWinner = random.randint(1, 100)
winnerWinner = 1
# print(winnerWinner)  # don't forget to comment this out when actually running the game!

while True:
    try:
        sleep(1.25)
        playerGuess = int(input("Pick a number, any number, between 1 and 100." + "\n"))
        if playerGuess < 1 or playerGuess > 100:
            raise ValueError
        break
    except ValueError:
        print("Invalid guess. The number must be between 1 and 100." + "\n")

attempts = 5
while attempts > 0:

    number = -1

    if playerGuess == winnerWinner:
        print("What a guess! You won!")
        break

    elif playerGuess < 1 or playerGuess > 100:
        print("Invalid guess. The number must be between 1 and 100." + "\n")
        number = 0

    elif 100 >= abs(winnerWinner - playerGuess) > 40:
        print ("What's it like living in the North Pole? Way cold! Here's an extra guess for free!")
        number = 1

    elif 40 >= abs(winnerWinner - playerGuess) > 20:
        print ("Still colder. Like, Minnesota cold!")

    elif 20 >= abs(winnerWinner - playerGuess) > 10:
        print("Getting warmer!" + "\n")

    elif 10 >= abs(winnerWinner - playerGuess) > 5:
        print("Starting to get hot!" + "\n")

    elif abs(winnerWinner - playerGuess) <= 5:
        print ("You're burning up! Red hot!")

    attempts = attemptUpdater(attempts, number)
    try:
        playerGuess = playerGuessText(attempts)
    except:
        print("Enter a valid number!")

if attempts == 0:
    print(f"You ran out of guesses. Nice try though! The correct number was {winnerWinner}")