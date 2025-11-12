# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
from Recipe import Recipe

class RecipeManager:
    ''' Attributes:
        - _recipes: list of Recipe objects -> [Recipe]
    '''
    def __init__(self):
        self._recipes = self.__read_from_psv()

    def __del__(self):
        self.__save_recipes(self._recipes)

    # MARK: - Private Data Mutators
    @staticmethod
    def __psv(data):
        if isinstance(data, list) or isinstance(data, tuple):
            return "|".join(data)
        return data

    def __recipe_to_psv(self, recipe) -> str:
        l = recipe.get_list()
        l = [RecipeManager.__psv(ele) for ele in l]
        return "|".join(str(ele).replace("|", "\\|") for ele in l)

    # MARK: - Private Handlers
    def __read_from_psv(self):
        recipes = list()
        with open("recipes.psv", "r") as file:
            for line in file:
                # TODO: Parse line ; use helper func
                pass

        # TODO: Add error handling for file
        return recipes

    def __save_recipes(self, recipes):
        success = True
        try:
            with open("recipes.psv", "w") as file:
                header = "Name", "Chef", "Ingredients", "Tools", "Rating", "Cooking Time", "Prep Time", "Total Time", "Date"
                file.write("|".join(header) + "\n")
                for recipe in recipes:
                    psv = self.__recipe_to_psv(recipe) + "\n"
                    file.write(psv)
        except IOError:
            success = False
            print("Unable to write recipes!")

        return success

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

    # Display all recipes.
    def display_all(self):
        i = 0
        while i < len(self._recipes):
            print(self._recipes[i])
        pass

    def search_for_recipe(self):
        # TODO: Implement search
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

    def sort_recipes(self):
        # TODO: Implement sort_recipes
        # Prompt to see how to sort
        pass

    def recommend_recipe(self):
        # TODO: Implement recommend_recipe
        # Prompt to see if it should rec based on duration, no ingredients, or something else
        pass

    def load_recipes(self) -> bool:
        # TODO: Implement load_recipe
        pass

    def save_recipes(self) -> bool:
        # TODO: Implement save_recipe
        success = False

        try:
            success = self.__save_recipes(self._recipes)
        except:
            print("Unknown error occurred during save process!")

        return success