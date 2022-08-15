"""
Question component
ask question and give appropriate output based on user input
v1 - set up questions and answer
"""


# Ask the user question
answer = input("What is this recipe? Dough, tomato sauce, cheese, pepperoni ")

# set a correct answer
if answer == "pizza":
    print("Correct")
# if the answer is incorrect tell the user the correct answer
else:
    print(f"The answer is 'pizza', not {answer!r}")

answer = input("What is this recipe? Pastry, mince meat, cheese, tomato sauce ")

if answer == "lasagne":
    print("Correct")
else:
    print(f"The answer is 'lasagne', not {answer!r}")

answer = input("What is this recipe? chicken,  rice, vegetables, soy sauce ")

if answer == "fried rice":
    print("Correct")
else:
    print(f"The answer is 'fried rice', not {answer!r}")

answer = input("tuna, rice, seaweed , avocado ? ")

if answer == "sushi":
    print("Correct")
else:
    print(f"The answer is 'sushi', not {answer!r}")

answer = input("What is this recipe? chicken,  broth, noodles, onion, carrot")

if answer == "chicken noodle soup":
    print("Correct")
else:
    print(f"The answer is 'sushi', not {answer!r}")
