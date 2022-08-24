# Guessing Game TODO
# Import the 'random' library
# Pick a random number between 1-50
# ask user to choose number
# tell them if its too high or too low or if they got it
# Let them guess 6 times then tell them the number

# Bonus: tell them how many guesses it took
# Exception/error handling

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

# if playerGuess > winnerWinner:
#     print("What's it like living in the North Pole? Way cold!")
# if playerGuess < winnerWinner:
#     print("Getting warmer.")
# elif playerGuess == winnerWinner:
#     print("What a great guess! You won!")

# if playerGuess is >30, say "What's it like living in the North Pole? Way cold!"
# if playerGuess guess is 20-30 from winnerWinner, then "
# if player guess is 10-20 numbers away, say "Getting warmer."
# if playerGuess is between 10-5 away from
# if playerGuess is within 5, say "getting red hot/You're burning up!"

#basic code for the game
    # elif playerGuess > winnerWinner:
    #     print("Nice try! Guess again!")
    #     sleep(0.5)
    #     playerGuess = int(input(f"Pick any guess between 1 and 100. You have {attempts} attempts remaining." + "\n"))
    #     attempts -= 1
    #
    # elif playerGuess < winnerWinner:
    #     print("Nice try! Guess again!")
    #     sleep(0.5)
    #     playerGuess = int(input(f"Pick any guess between 1 and 100. You have {attempts} attempts remaining." + "\n"))
    #     attempts -= 1


