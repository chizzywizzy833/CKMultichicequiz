# function go here...

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


# main routine
display_instructions = yes_no("Have you played the game before? ")

if display_instructions == "no":
    print('Display instructions')
else:
    print("Programs continues")
