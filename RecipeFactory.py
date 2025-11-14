from datetime import datetime, time

from MasterTime import MasterTime
from Recipe import Recipe


class RecipeFactory:
    @staticmethod
    def create_from_array(arr):
        """Could raise RecipeMalformedError"""
        try:
            psv_separated = arr.split("|")

            name = psv_separated[0]
            chef = psv_separated[1]
            ingredients = psv_separated[2]
            tools = psv_separated[3]
            rating = int(psv_separated[4])
            cook_time = RecipeFactory.__time_from_str(psv_separated[5])
            prep_time = RecipeFactory.__time_from_str(psv_separated[6])
            total_time = RecipeFactory.__time_from_str(psv_separated[7])
            date_created = RecipeFactory.__ts_from_str(psv_separated[8])
            date_updated = RecipeFactory.__ts_from_str(psv_separated[9])

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


class RecipeMalformedError(Exception):
    def __init__(self, message, code=None):
        super.__init__(message)
        self.message = message
        self.code = code


