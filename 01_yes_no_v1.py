# Ask the user if they have played before
display_instructions = input("Have you played my quiz before? ").lower()

# if user says yes = 'program continues'
if display_instructions == "yes":
    print("Program continues")

elif display_instructions == "y":
    print("display instructions")

elif display_instructions == "no":
    print("display instructions")

elif display_instructions == 'n':
    print("display instructions")


# If user says no = 'display instructions'
else:
    print("Please answer with either yes / no")
