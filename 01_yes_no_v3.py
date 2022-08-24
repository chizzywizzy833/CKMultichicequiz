"""
yes_no checker component
v1 - set up yes and checker
v2 - make code more efficient using or statements
v3 - turn v2 code into  a function and add to base component v1
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


# main routine goes here ***************

# call yes and no function
display_instructions = yes_no("Have you played the game before? ")

print("You choose {}".format(display_instructions))
