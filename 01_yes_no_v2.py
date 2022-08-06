display_instructions = ""
while display_instructions.lower() != "xxx":
    # Ask the user if they have played before
    display_instructions = input("Have you played this quiz before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error

    if display_instructions == "yes" or display_instructions == "y":
        print("program continues")

    elif display_instructions == "no" or display_instructions == "n":
        print("display instructions")

    else:
        print("please answer either Yes / No")
