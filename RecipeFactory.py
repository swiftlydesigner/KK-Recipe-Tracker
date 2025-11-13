
class RecipeFactory:
    @staticmethod
    def create_from_array(arr):
        """Could raise RecipeMalformedError"""
        try:
            psv_separated = arr.split("|")

            name = psv_separated[0]
            chef = psv_separated[1]
            # self.__name = name
            # self.__chef = chef
            # self.__ingredients = ingredients
            # self.__tools = tools
            # self.__rating = rating
            # self.__cooking_time = cooking_time
            # self.__prep_time = prep_time
            # self.__total_time = total_time
            # self.__date_created = date_created if not None else datetime.now()
            # self.__date_updated = date_updated if not None else datetime.now()
        except:
            raise RecipeMalformedError("Input recipe list was malformed!", 0x01)


class RecipeMalformedError(Exception):
    def __init__(self, message, code=None):
        super.__init__(message)
        self.message = message
        self.code = code


