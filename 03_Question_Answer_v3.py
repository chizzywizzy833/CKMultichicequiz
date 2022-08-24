"""
Question component
display recipes and give appropriate output based on user input
v1 - set up recipes and answer
"""

# Import libraries go here **************************
from string import ascii_lowercase

"""
Below is a dictionary has been set up. 
A dictionary is used to store data values in key and value pairs.
in this case the list of the ingredients acts as the key
while the pairs stores the correct recipe for that set of ingredients and the alternative options

"""

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
-By using enumerate I can iterate through a sequence in this case 
i use it to number of each question

- To get characters that label my alternatives, use string.ascii lowercase. 
With zip(), I mix letter and alternatives and save them in a dictionary.

-\n = new line 
"""
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
        print("⭐ Correct! ⭐")
    else:
        print(f"The answer is {correct_recipe!r}, not {answer!r}")
