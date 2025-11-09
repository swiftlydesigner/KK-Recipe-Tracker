# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00

# IoManager.py
## This file will contain printing and reading input from users

class IoManager:
    def __init__(self):
        raise Exception("Fatal: Cannot create an instance of IoManager")
        pass # No setup required

    @staticmethod
    def _get_input(self, message):
        ''' Gets input from the user with a pre-defined format.'''
        return input(f"{message}\n> ")

    @staticmethod
    def read_str(self, message, empty_ok=True, error=False):
        '''Prints the message, and returns a valid string from the user.'''

        if error:
            print("Bad user input. Please enter a valid string.", end='')
            print("" if empty_ok else " Empty strings are INVALID.")

        response = self._get_input(message)

        # Check if empty is acceptable and enforce rules
        if not empty_ok and len(response) == 0:
            response = self.read_str(message, empty_ok, error=True)

        return response

    @staticmethod
    def read_int(self, message, error=False):
        '''Will read an int from the user and return a valid integer.'''

        # Note to programmer: Use try/catch to convert into int and use similar pattern to read_str (call itself and set error to True. Also add error check adding the message as above.)
        pass

    @staticmethod
    def read_float(self, message, error=False):
        '''Will read a float from the user and return a valid float.'''
        pass


