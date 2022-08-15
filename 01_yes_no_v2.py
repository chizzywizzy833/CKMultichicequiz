"""
yes_no checker component
v1 - set up yes and checker
v2 - make code more efficient using or statements
"""

# this is a loop that makes it easier for testing
display_instructions = ""
while display_instructions.lower() != "xxx":

    # Ask the user if they have played before
    display_instructions = input("Have you played this quiz before? ").lower()

    # If they say yes, output 'program continues'
    if display_instructions == "yes" or display_instructions == "y":
        print("program continues")

    # If they say no, output 'display instructions
    elif display_instructions == "no" or display_instructions == "n":
        print("display instructions")

    # If the answer is invalid, print an error
    else:
        print("please answer either Yes / No")
