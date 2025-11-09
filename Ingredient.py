# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
#---------DONE----------
from Unit import Unit

class Ingredient:
    ''' Attributes:
        - _name -> str
        - _quantity -> Unit
    '''
    def __init__(self, name, quantity):
        self._name = name
        self._quantity = quantity

    # MARK: Setters and Getters
    def name(self):
        return self._name

    def update_name(self, name):
        self._name = name

    def amount(self):
        return self._quantity

    def update_amount(self, amount):
        self._quantity = amount

