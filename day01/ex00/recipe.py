class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if not isinstance(name, str):
            raise ValueError("name is not a string")
        if not name:
            raise ValueError("name is empty")
        if not isinstance(cooking_lvl, int):
            raise ValueError("cooking_lvl is not a int")
        if cooking_lvl < 1 or cooking_lvl > 5:
            raise ValueError("cooking_lvl is not between 1 and 5 included")
        if not isinstance(cooking_time, int):
            raise ValueError("cooking_time is not a int")
        if cooking_time < 0:
            raise ValueError("cooking_time is negative")
        if (not isinstance(ingredients, list)
                or any(not isinstance(x, str) for x in ingredients)):
            raise ValueError("ingredients is not a list of strings")
        if not ingredients:
            raise ValueError("ingredients is empty")
        if not isinstance(description, str):
            raise ValueError("description is not a string")
        if not isinstance(recipe_type, str):
            raise ValueError("recipe_type is not a string")
        if recipe_type not in ('starter', 'lunch', 'dessert'):
            raise ValueError("recipe_type is not 'starter',"
                             "'lunch' or 'dessert'")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return ', '.join([f'{key}: {value}' for key, value
                          in self.__dict__.items()])
