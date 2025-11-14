from datetime import datetime, time

from Ingredient import Ingredient
from MasterTime import MasterTime
from Recipe import Recipe


class RecipeFactory:
    @staticmethod
    def create_from_psv_line(line):
        """Could raise RecipeMalformedError"""
        try:
            psv_separated = line.split("|")

            name = psv_separated[0].strip()
            chef = psv_separated[1].strip()
            ingredients = RecipeFactory.__gen_list_ingredients(psv_separated[2].strip())
            tools = RecipeFactory.__list_from_csv(psv_separated[3].strip())
            rating = float(psv_separated[4].strip())
            cook_time = RecipeFactory.__time_from_str(psv_separated[5].strip())
            prep_time = RecipeFactory.__time_from_str(psv_separated[6].strip())
            total_time = RecipeFactory.__time_from_str(psv_separated[7].strip())
            date_created = RecipeFactory.__ts_from_str(psv_separated[8].strip())
            date_updated = RecipeFactory.__ts_from_str(psv_separated[9].strip())

            return Recipe(name, chef, ingredients, tools, rating,
                          cook_time, prep_time, total_time,
                          date_created, date_updated)

        except ValueError:
            raise RecipeMalformedError("Expected rating to be type int!", 0x02)
        except:
            raise RecipeMalformedError("Input recipe list was malformed!", 0x01)

    @staticmethod
    def __time_from_str(string):
        time_format = "%H:%M:%S"
        dt_data = datetime.strptime(string, time_format)
        return dt_data.time()

    @staticmethod
    def __ts_from_str(ts):
        return MasterTime.ts_from_str(ts)

    @staticmethod
    def __gen_list_ingredients(ingredients):
        ingredient_list = []

        for ingredient in ingredients.split(","):
            result = RecipeFactory.__ingredient_from_str(ingredient)
            if result is not None:
                ingredient_list.append(result)

        return ingredient_list

    @staticmethod
    def __ingredient_from_str(ingredient):
        ingredient_obj = None # dead store, but easier to read
        parts = ingredient.split("?")

        if len(parts) == 3:
            ingredient_obj = Ingredient(parts[0], float(parts[1]), parts[2])
        elif len(parts) == 2:
            ingredient_obj = Ingredient(parts[0], float(parts[1]), None)
        elif len(parts) == 1:
            ingredient_obj = Ingredient(parts[0], None, None)

        return ingredient_obj

    @staticmethod
    def __list_from_csv(string):
        return string.split(",")


class RecipeMalformedError(Exception):
    def __init__(self, message, code=None):
        super.__init__(message)
        self.message = message
        self.code = code


