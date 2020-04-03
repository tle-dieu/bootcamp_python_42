import re

cookbook = {'sandwich':
            {'ingredients': ['ham', 'bread', 'cheese', 'tomatoes'],
             'meal': 'lunch',
             'prep_time': 10},
            'cake':
            {'ingredients': ['flour', 'sugar', 'eggs'],
             'meal': 'dessert',
             'prep_time': 60},
            'salad':
            {'ingredients': ['avocado', 'arugula', 'tomatoes', 'spinach'],
             'meal': 'lunch',
             'prep_time': 15}}


def add_recipe(recipe_name, ingredients, meal, prep_time):
    cookbook[recipe_name] = {
        'ingredients': ingredients,
        'meal': meal,
        'prep_time': prep_time,
    }


def recipe_parser():
    name_recipe = ''
    while not name_recipe:
        name_recipe = input("Please enter the recipe's name:\n>> ")
    print("\nPlease enter the ingredients separated by comma:")
    ingredients = list(filter(None, re.split(r'\s*,\s*', input('>> '))))
    meal = ''
    while not meal:
        meal = input("\nPlease enter the meal type:\n>> ")
    prep_time = ''
    while not prep_time.isdigit():
        prep_time = input("\nPlease enter the preparation time:\n>> ")
    return(name_recipe, ingredients, meal, int(prep_time))


def delete_recipe(recipe_name):
    if not cookbook.pop(recipe_name, None):
        print("\nRecipe doesn't exist")
    else:
        print(f"\n{recipe_name.capitalize()} deleted")


def print_recipe(recipe_name):
    print('')
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:",
              f"Ingredients list: {recipe['ingredients']}",
              f"To be eaten for {recipe['meal']}",
              f"Takes {recipe['prep_time']} "
              f"minute{'s' if recipe['prep_time'] > 1 else ''}",
              sep='\n')
    else:
        print("Recipe doesn't exist")


def print_cookbook():
    print('\nCookbook: ')
    for recipe_name, recipe in cookbook.items():
        print(f"\t\n{recipe_name.capitalize()}:",
              f"\tIngredients list: {recipe['ingredients']}",
              f"\tTo be eaten for {recipe['meal']}",
              f"\tTakes {recipe['prep_time']} "
              f"minute{'s' if recipe['prep_time'] > 1 else ''}",
              sep='\n')


print("Please select an option by typing the corresponding number:",
      "1: Add a recipe",
      "2: Delete a recipe",
      "3: Print a recipe",
      "4: Print the cookbook",
      "5: Quit", sep='\n')
while True:
    entry = input('>> ').strip()
    print('')
    if entry == '1':
        add_recipe(*recipe_parser())
    elif entry == '2':
        delete_recipe(input("Please enter the recipe's name:\n>> "))
    elif entry == '3':
        print_recipe(input("Please enter the recipe's name:\n>> "))
    elif entry == '4':
        print_cookbook()
    elif entry == '5':
        print("Cookbook closed.")
    else:
        print("This option does not exist,"
              "please type the corresponding number.\n"
              "Type 5 to exit")
        continue
    break
