from __future__ import absolute_import
from datetime import datetime
from recipe import Recipe


class Book:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("name is not a string")
        if not name:
            raise ValueError("name is empty")
        self.name = name
        self.creation_date = datetime.now()
        self.last_update = datetime.now()
        self.recipes_list = {'starter': {}, 'lunch': {}, 'dessert': {}}

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        recipe = next((x[name] for x in self.recipes_list.values()
                       if name in x), None)
        if not recipe:
            raise ValueError(f"'{name}' doesn't exist in recipe_list")
        return recipe

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        return list(self.recipes_list[recipe_type].keys())

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise ValueError('recipe is not a type Recipe')
        self.last_update = datetime.now()
        self.recipes_list[recipe.recipe_type][recipe.name] = recipe
