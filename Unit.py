# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00

class Unit:
    ''' Attributes:
        - _qty -> float
        - _name -> str

    '''
    def  __init__(self, qty, name):
        self._qty = qty
        self._name = name

    def qty(self):
        return self._qty
    def name(self):
        return self._name
        
