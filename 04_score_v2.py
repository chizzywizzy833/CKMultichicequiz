"""
Score component
v1- if user guess the correct recipe add 1 to the score
v2- display score st the end of the program
"""

# Import libraries go here **************************
from string import ascii_lowercase

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


"""
make a variable and set it to equal 0 
When user guess the correct recipe add +1 to the variable 
display score at the end of the program 

"""

score = 0
for num, (recipe, alternatives) in enumerate(Ingredients.items(), start=1):
    print(f"\nIngredients list {num}:")
    print(f"{recipe}?")
    correct_recipe = alternatives[3]
    labeled_alternatives = dict(zip(ascii_lowercase, sorted(alternatives)))
    for label, alternative in labeled_alternatives.items():
        print(f"  {label}) {alternative}")

    while (answer_label := input("\nWhat is this recipe? ")) not in labeled_alternatives:
        print(f"sorry that's not a valid answer. Please choose a,b,c,d")

    answer = labeled_alternatives[answer_label]
    if answer == correct_recipe:
        score += 1
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_recipe!r}, not {answer!r}")

print(f"\nYou got {score} out of 10 recipes correct")
