# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
from Menu import Menu

from IoManager import IoManager # Usage: IoManager.method
from RecipeManager import RecipeManager # Usage: RecipeManager().method

class Application:
        ''' Attributes:
            - __manager -> RecipeManager
            - __menu -> Menu
        '''
        def __init__(self):
            self.__manager = RecipeManager()
            self.__menu = Menu({
                "Display Recipes" : self.__display_recipes(),
                "Add Recipe" : self.__add_recipe(),
                "Remove Recipe" : self.__remove_recipe(),
                "Edit Recipe" : self.__edit_recipe(),
                "Sort Recipes" : self.__sort_recipes(),
                "Recommend Recipe" : self.__reccomend_recipe(),
                "Load Recipes" : self.__load_recipes(),
                "Save Recipes" : self.__save_recipes(),
                "Exit" : self.__exit()
            })

        def __perform_menu_interaction(self):
            self.__menu.show_menu()
            option = self.__menu.get_user_response()
            success = self.__menu.handle_user_response(option)

            if not success:
                print("Failed to run the menu script!")


        def runApp(self):
            input_str = IoManager.get_str("What is your name?")
            input_str_non_empty = IoManager.get_str("What is your City?", empty_ok=False)

            print(f"Your name is {input_str}\nYour city is {input_str_non_empty}.")

# MARK: - Actions

        def __display_recipes(self):
            self.__manager.display_all()

        def __add_recipe(self):
            self.__manager.add_recipe()

        def __remove_recipe(self):
            self.__manager.remove_recipe()

        def __edit_recipe(self):
            self.__manager.edit_recipe()

        def __sort_recipes(self):
            self.__manager.sort_recipes()

        def __reccomend_recipe(self):
            pass

        def __load_recipes(self):
            pass

        def __save_recipes(self):
            pass

        def __exit(self):
            pass

