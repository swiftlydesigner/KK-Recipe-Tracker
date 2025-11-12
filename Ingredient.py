# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
#---------DONE----------
from Unit import Unit


class Ingredient:
    ''' Attributes:
        - __name -> str
        - __quantity -> float
        - __unit -> str
    '''

    def __init__(self, name, quantity, unit):
        self.__name = name
        self.__quantity = quantity
        self.__unit = unit

    # MARK: Setters and Getters
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def amount(self):
        return self.__quantity

    @amount.setter
    def amount(self, amount):
        self.__quantity = amount

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, unit):
        self.__unit = unit
