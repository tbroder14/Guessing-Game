# Contact List App TODO
# ask user if they want to add, edit or view a contact dictionary
# if they want to view it then show the entire dictionary of names and numbers
# if they want to add then ask for a name and number and add to the contact list
# if they want to edit ask them which name to edit then what the updated number should be
# after getting updated info to edit show them the updated name/number
#
# Example of a Dictionary
# contacts = { "josh": "123-123-1234", "jordan": "234-234-2345" }
# print(contacts{"josh"})
# output: 123-123-1234
#
# NOTES
# Python "Dictionaries" cannot have duplicate keys, so you can't have 2 "josh" in your list (it will just overwrite original)
# If someone tries to add a name that already exists ask if they
# would like to instead edit the current record of that name or change that name to something else

# Bonus
# When a number is added/edited make sure it is a 10 digit long number and add hyphens if user does not include them
# Hint: use "Regex" or "Regular expression" good luck lol

# Super Bonus
# Create a new GitHub repo and push this project to it

# Super Duper Bonus
# save data between executions of the program by saving to a .txt file
# Hint: http://automatetheboringstuff.com/2e/chapter9/
# You don't need to read the whole thing, but it has info about reading/writing to a file

from time import sleep
from newContact import *
from editContact import *
import pprint

sleep(0.5)
print("Welcome to your contacts list!")
sleep(0.85)

contacts = {}

while True:

    selection = input("Would you like to add a new contact [N], edit an existing contact [E], or view your entire contact list [V]?" + "\n")

    if selection == ("N" or "n"):
        contacts = newContact(contacts)
        print(contacts)
        while True:
            mmAfterNew = input("Would you like to add an additional new contact [N] or return to the main menu [M]?" + "\n")
            if mmAfterNew == ("N" or "n"):
                contacts = newContact(contacts)
                print(contacts)
            else:
                break
                # need to figure out a way to actually return to the main menu

    elif selection == ("E" or "e"):
        contacts = editContact(contacts)
        while True:
            mmAfterEdit = input("Would you like to edit another contact [N] or return to the main menu [M]?" + "\n")
            if mmAfterNew == ("N" or "n"):
                contacts = newContact(contacts)
                print(contacts)
            else:
                break



    elif selection == ("V" or "v"):
        print(contacts)
        sleep(2)
        while True:
            selection = input("Would you like to return to the main menu [M]?" + "\n")
            if selection == ("M" or "m"):
                break

    else:
        print("Please select a valid option by typying either [N], [E], or [V].")
        continue


# have to make the code loop after this error; otherwise, the program stops if the use inputs an incorrect option
# Questions for josh
# Why do lowercase answers not work when it's ("M" or "m")?
# If line 55 is selection = "N" or "n" (without the parenthesis), why it the code not break if you put in "M" or literally anything else?
# how to get the contacts to be printed with a line break? pretty.print doesn't seem to work with a dictionary


