"""
instructions component
print instruction or continue program based on user input
v1 - add yes and no checker to test with instruction component
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
display_instructions = yes_no("Have you played the game before? ")

if display_instructions == "no":
    print('Display instructions')
else:
    print("Programs continues")
