"""
base component for the Guess the recipe
V0 - skeleton setup
v1 - yes and no checker has been added
v2 - working instructions has been added
author- Chisomo Kamphambe
CC CLK 2022
"""


# Import libraries go here **************************

# functions go here **************************

def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("Please answer yes / no")


def instructions():
    print("****How to play****")
    print()
    print("The rules of the game")
    print()
    return ""


# main routine goes here ***************

# call function yes_no
played_before = yes_no("Have you played the game before? ")

print("You choose {}".format(played_before))

# call function instructions
if played_before == "no":
    instructions()

print("Program continues")
