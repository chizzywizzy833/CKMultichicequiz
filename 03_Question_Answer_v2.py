"""
Question component
display recipes and give appropriate output based on user input
v1 - ask user question
v2 - add questions into list with an answer
"""
# Make list with question and assigned an answer
Ingredients = [
    ["What is this recipe? Dough, tomato sauce, cheese, pepperoni", 'pizza'],
    ["What is this recipe? Pastry, mince meat, cheese, tomato sauce", 'lasagne'],
    ["What is this recipe? chicken,  rice, vegetables, soy sauce", 'fried rice'],
    ["What is this recipe? tuna, rice, seaweed , avocado", "sushi"],
    ["What is this recipe? chicken,  broth, noodles, onion, carrot", "chicken noodle soup"],
    ["What is this recipe? cinnamon, brown sugar, pastry, icing sugar", "cinnamon rolls"],
    ["What is this recipe? Cream cheese, crushed cookies, lemon, butter", "lemon cheesecake"],
    ["What is this recipe? Egg white, Strawberry, whipped cream, blueberries", "pavlova"],
    ["What is this recipe? Bread, milk, egg, cinnamon", "french toast"],
    ["What is this recipe? Brown sugar, chocolate chips, sugar, Flour", "chocolate chip cookies"],


]
# loop to ask each recipe in list
for question, correct_recipe in Ingredients:
    answer = input(f"{question}? ")
    if answer == correct_recipe:
        print("Correct!")
# print correct answer and then print users answer
    else:
        print(f"The answer is {correct_recipe!r}, not {answer!r}")
