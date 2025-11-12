# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
from IoManager import IoManager


class Menu:
    def __init__(self, actions):
        self.__items = actions

    def __validate_input(self, selection):
        valid = selection is not None

        if not isinstance(selection, int):
            valid = False

        # Check for valid to ensure it is of type int to guarantee > and < op compatability
        if valid and (selection < 0 or selection > len(self.__items)):
            valid = False

        return valid


    def show_menu(self):
        item = 1
        if self.__items is not None: # Avoid exception
            print("0) Cancel")
            for name in self.__items.keys():
                print(f"{item}) {name}")
                item += 1
        else:
            print("No available options!")

    def get_user_response(self):
        user_response = -1
        if self.__items is not None: # Avoid exception
            while not self.__validate_input(user_response): # validate user choice
                user_response = IoManager.get_int("What would you like to do? (enter line number)")

        return user_response

    def handle_user_response(self, user_response):
        success = False
        if self.__items is not None:
            if user_response != 0:
                key = sorted(self.__items.keys())[user_response - 1]
                func = self.__items[key]
                func()
                success = True
            # else, do nothing

        return success