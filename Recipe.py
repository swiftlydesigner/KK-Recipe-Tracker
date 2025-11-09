# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00

from Ingredient import Ingredient

from datetime import datetime

class Recipe:
    ''' Attributes:
        - _name -> str
        - _chef -> str
        - _ingredients -> [Ingredient]
        - _tools -> [str]
        - _rating -> flat
        - _cooking_time -> datetime.time
        - _prep_time -> datetime.time
        - _total_time -> datetime.time
        - _date_created -> datetime
        - _date_updated -> datetime
    '''
    def __init__(self, name=None, chef=None, ingredients=None, tools=None, rating=None, 
             cooking_time=None, prep_time=None, total_time=None, date_created=None):
        self._name = name
        self._chef = chef
        self._ingredients = ingredients
        self._tools = tools
        self._rating = rating
        self._cooking_time = cooking_time
        self._prep_time = prep_time
        self._total_time = total_time
        self._date_created = date_created if not None else datetime.now()
        self._date_updated = date_updated if not None else datetime.now()

    # MARK: - Getters and setters
    def name(self):
        return self._name

    def update_name(self, name):
        self._name = name
        self._date_updated = datetime.now()

    def chef(self):
        return self._chef

    def update_chef(self, chef):
        self._chef = chef
        self._date_updated = datetime.now()

    def ingredients(self):
        return self._ingredients

    def update_ingredients(self, ingredients):
        self._ingredients = ingredients
        self._date_updated = datetime.now()

    def tools(self):
        return self._tools

    def update_tools(self, tools):
        self._tools = tools
        self._date_updated = datetime.now()

    def rating(self):
        return self._rating

    def update_rating(self, rating):
        self._rating = rating
        self._date_updated = datetime.now()

    def cooking_time(self):
        return self._cooking_time

    def update_cooking_time(self, cooking_time):
        self._cooking_time = cooking_time
        self._date_updated = datetime.now()

    def prep_time(self):
        return self._prep_time

    def update_prep_time(self, prep_time):
        self._prep_time = prep_time
        self._date_updated = datetime.now()

    def total_time(self):
        return self._total_time

    def update_total_time(self, total_time):
        self._total_time = total_time
        self._date_updated = datetime.now()


    # The following dates to not have a setter as they should not be modified except by internal mechanics
    def date_created(self):
        return self._date_created

    def date_updated(self):
        return self._date_updated

