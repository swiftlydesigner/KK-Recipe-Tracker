# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00

class RecipeManager:
    ''' Attributes:
        - _recipes: list of Recipe objects -> [Recipe]
    '''
    def __init__(self):
        self._recipes = self.__read_from_psv()

    def __del__(self):
        self.__save_recipes(self._recipes)

    def __read_from_psv(self):
        recipes = list()
        with open("recipes.psv", "r") as file:
            for line in file:
                # TODO: Parse line ; use helper func
                pass

        # TODO: Add error handling for file
        return recipes

    def __save_recipes(self, recipes):
        # TODO: Open file and write header
        for recipe in recipes:
            # TODO: Write recipe
            pass

        # TODO: Add error handling for file

    def __search_for_recipe(self, name):
        # TODO: Use linear search
        # TODO: If there is time, use binary search

        pass

    def __sort_recipes_by_time(self):
        # TODO: Use bubble sort, based off time
        for i in range(self._recipes):
            for j in range(i, self._recipes):
                # Swap i and j if ele[i] > ele[j]
                pass

    def __sort_recipes_by_name(self):
        # TODO: Use bubble sort, based off name of recipe
        pass

    def __sort_recipes_by_date(self):
        # TODO: Use bubble sort, based off date created
        pass

    def __sort_recipes_by_rating(self):
        # TODO: Use bubble sort, based off rating
        pass

    def display_all(self):
        # TODO: Implement display_all
        pass

    def add_recipe(self):
        # TODO: Implement add_recipe
        pass

    def remove_recipe(self):
        # TODO: Implement remove_recipe()
        pass

    def edit_recipe(self):
        # TODO: Implement edit_recipe
        pass
