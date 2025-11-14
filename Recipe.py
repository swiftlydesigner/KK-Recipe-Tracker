# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00


#-------------DONE----------------

from MasterTime import MasterTime
from datetime import datetime

class Recipe:
    ''' Attributes:
        - __name -> str
        - __chef -> str
        - __ingredients -> [Ingredient]
        - __tools -> [str]
        - __rating -> float
        - __cooking_time -> datetime.time
        - __prep_time -> datetime.time
        - __total_time -> datetime.time
        - __date_created -> datetime
        - __date_updated -> datetime
    '''

    def __init__(self, name=None, chef=None, ingredients=None, tools=None, rating=None,
                 cooking_time=None, prep_time=None, total_time=None, date_created=datetime.now(), date_updated=datetime.now()):
        self.__name = name
        self.__chef = chef
        self.__ingredients = ingredients
        self.__tools = tools
        self.__rating = rating
        self.__cooking_time = cooking_time
        self.__prep_time = prep_time
        self.__total_time = total_time
        self.__date_created = date_created
        self.__date_updated = date_updated

    # Using as a human-readable stringify method.
    def __str__(self):
        return (f"{self.__name}: Created by {self.__chef} [{int(self.__rating) * "*"}{int(5 - self.__rating) * " "}]"
                f"Total Time: {self.__total_time}, Prep Time: {self.__prep_time}, Cooking Time: {self.__cooking_time}")

    # MARK: - Getters and setters
    def get_list(self):
        return [self.__name, self.__chef, self.__ingredients, self.__tools, self.__rating,
                self.__cooking_time, self.__prep_time, self.__total_time, MasterTime.ts_to_str(self.__date_created), MasterTime.ts_to_str(self.__date_updated)]

    def name(self):
        return self.__name

    def update_name(self, name):
        self.__name = name
        self.__date_updated = datetime.now()

    def chef(self):
        return self.__chef

    def update_chef(self, chef):
        self.__chef = chef
        self.__date_updated = datetime.now()

    def ingredients(self):
        return self.__ingredients

    def update_ingredients(self, ingredients):
        self.__ingredients = ingredients
        self.__date_updated = datetime.now()

    def tools(self):
        return self.__tools

    def update_tools(self, tools):
        self.__tools = tools
        self.__date_updated = datetime.now()

    def rating(self):
        return self.__rating

    def update_rating(self, rating):
        self.__rating = rating
        self.__date_updated = datetime.now()

    def cooking_time(self):
        return self.__cooking_time

    def update_cooking_time(self, cooking_time):
        self.__cooking_time = cooking_time
        self.__date_updated = datetime.now()

    def prep_time(self):
        return self.__prep_time

    def update_prep_time(self, prep_time):
        self.__prep_time = prep_time
        self.__date_updated = datetime.now()

    def total_time(self):
        return self.__total_time

    def update_total_time(self, total_time):
        self.__total_time = total_time
        self.__date_updated = datetime.now()

    # The following dates do not have a setter as they should not be modified except by internal mechanics
    def date_created(self):
        return self.__date_created

    def date_updated(self):
        return self.__date_updated
