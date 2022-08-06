
display_instructions = ""
while display_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error
    if display_instructions == "yes":
        print("program continues")

    elif display_instructions == "y":
        print("program continues")

    elif display_instructions == "no":
        print("display instruction")

    elif display_instructions == "n":
        print("display instructions")

    # If they say no, output "display instructions"
    else:
        print("please answer either yes / no")
