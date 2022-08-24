"""
base component for the Guess the recipe
V0 - skeleton setup
v1 - yes and no checker has been added
v2 - working instructions has been added
v3 - working question component has been added
author- Chisomo Kamphambe
CC CLK 2022
"""

# Import libraries go here **************************
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
            print("Please answer yes / no")


# depending on user input yes = start game  no = show instructions then start game
def instructions():
    print("****How to play****")
    print()
    print("The rules of the game")
    print()
    return ""


# main routine goes here ***************

played_before = yes_no("Have you played the game before? ")

print("You choose {}".format(played_before))

if played_before == "no":
    instructions()

# dictionary for questions and answer
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

# number the questions starting at 1
for num, (recipe, alternatives) in enumerate(Ingredients.items(), start=1):
    print(f"\nIngredients list {num}:")
    print(f"{recipe}?")
    correct_recipe = alternatives[3]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    # if user puts in guess that is not in dictionary (invalid answer) loop question again until user puts a valid answer
    while (answer_label := input("\nWhat is this recipe? ")) not in labeled_alternatives:
        print(f"sorry that's not a valid answer. Please choose a,b,c,d")

    answer = labeled_alternatives[answer_label]
    if answer == correct_recipe:
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_recipe!r}, not {answer!r}")
