"""
base component for the Guess the recipe
V0 - skeleton setup
v1 - yes and no checker has been added
v2 - working instructions has been added
v3 - working question component has been added
V3.1 - randomization = every time you will be asked all the question in a different order if your resset the program &
added functions to shorten code
v4 - working score component
working game v1 -
author- Chisomo Kamphambe
CC CLK 2022
"""

# Import libraries go here **************************
import random
from string import ascii_lowercase


# functions go here **************************

# check for yes and no
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
            print("Sorry that's not the answer im looking for. Try again ")


# depending on user input yes = start game  no = show instructions then start game
def instructions():
    print("****How to play****")
    print()
    print("""
You will be given a list of ingredients for a certain dish. It is up to you to
guess the recipe from that list of ingredients.Please do this by selecting a,b,c or d
There are ten question in the game, and you'll be scored out of ten.
    """)
    print()
    return ""


# start quiz
def run_quiz():
    questions = prepare_questions(
        Ingredients, num_questions=NUM_QUESTIONS_PER_QUIZ
    )

    score = 0
    for num, (question, alternatives) in enumerate(questions, start=1):
        print(f"\n***QUESTION*** {num}:")
        score += ask_question(question, alternatives)

    print(f"\nYou got {score} out of 10 recipes correct")


# prepare the question putting them in order and numbering alternatives
def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


# ask question
def ask_question(question, alternatives):
    correct_answer = alternatives[3]
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))

    answer = get_answer(question, ordered_alternatives)
    if answer == correct_answer:
        print("⭐ Correct! ⭐")
        return 1
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
        return 0


# decide an output based a user input
def get_answer(question, alternatives):
    print(f"{question}?")
    labeled_alternatives = dict(zip(ascii_lowercase, alternatives))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\n***What is this recipes***? ")) not in labeled_alternatives:
        print(f"***sorry that's not a valid answer. Please choose a,b,c,d***")

    return labeled_alternatives[answer_label]


# main routine goes here ***************

print("***GUESS THE RECIPE***")

played_before = yes_no("Have you played the game before? ")

print("You choose {}".format(played_before))

if played_before == "no":
    instructions()

# Ask all 10 question from the dictionary
NUM_QUESTIONS_PER_QUIZ = 10
Ingredients = {
    " Dough, tomato sauce, cheese, pepperoni": [
        "burger ", "taco", "salad", "pizza"
    ],
    " Pastry, mince meat, cheese, tomato sauce": [
        "blueberry pie", "steak and cheese pie", "cottage pie", "lasagne"
    ],
    " chicken,  rice, vegetables, soy sauce": [
        "rice pudding", "rice risotto", "stir fry", "fried rice"
    ],
    " tuna, rice, seaweed , avocado": [
        "Maki", "Nigiri", "sashimi", "sushi"
    ],

    "chicken,  broth, noodles, onion, carrot": [
        "mushroom soup", "pumpkin soup", "puree", "chicken noodle soup"

    ],

    "Brown sugar, chocolate chips, sugar, Flour": [
        "Shortbread", "Gingerbread", "fruit cake", "chocolate chip cookies"

    ],

    "Bread, milk, egg, cinnamon": [
        "pancakes", "waffles", "crumpets", "french toast"

    ],

    " Egg white, Strawberry, whipped cream, blueberries": [
        "scrambled white eggs", "Macaroon", "Meringue", "pavlova"

    ],

    "Cream cheese, crushed cookies, lemon, butter": [
        "chocolate cake", "Keylime cheese cake", "white chocolate raspberry", "lemon cheesecake"

    ],

    "cinnamon, brown sugar, pastry, icing sugar ": [
        "Savoury pinwheel", "Strawberry pastry", "Quiche", "cinnamon roll"

    ],

}

# execute some code only if the file was run directly, and not imported.
if __name__ == "__main__":
    run_quiz()
