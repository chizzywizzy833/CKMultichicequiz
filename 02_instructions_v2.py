"""
instructions component
print instruction or continue program based on user input
v1 - add yes and no checker to test with instruction component
v2 - make instructions component into function, so it is easy to call
"""


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

played_before = yes_no("Have you played the game before? ")

print("You choose {}".format(played_before))

if played_before == "no":
    instructions()

print("Program continues")
