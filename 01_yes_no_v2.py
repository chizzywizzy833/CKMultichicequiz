display_instructions = ""
while display_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = input("Have you played this game before? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error
    if display_instructions == "yes" or display_instructions == "y":
        display_instructions = "yes"
        print("program continues")

    elif display_instructions == "no" or display_instructions == "n":
        display_instructions = "no"
        print("display instruction")

    # If they say anything else, output "please answer yes / no"
    else:
        print("please answer either yes / no")
