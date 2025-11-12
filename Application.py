# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
import sys

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
                "Search for Recipe": self.__search_for_recipe(),
                "Add Recipe" : self.__add_recipe(),
                "Remove Recipe" : self.__remove_recipe(),
                "Edit Recipe" : self.__edit_recipe(),
                "Sort Recipes" : self.__sort_recipes(),
                "Recommend Recipe" : self.__recommend_recipe(),
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

            return success


        def run_app(self):
            # Run the menu, unless an error occurs, then exit the process
            while self.__perform_menu_interaction(): pass

# MARK: - Actions

        def __display_recipes(self):
            self.__manager.display_all()

        def __search_for_recipe(self):
            self.__manager.search_for_recipe()

        def __add_recipe(self):
            self.__manager.add_recipe()

        def __remove_recipe(self):
            self.__manager.remove_recipe()

        def __edit_recipe(self):
            self.__manager.edit_recipe()

        def __sort_recipes(self):
            self.__manager.sort_recipes()

        def __recommend_recipe(self):
            self.__manager.recommend_recipe()

        def __load_recipes(self):
            self.__manager.load_recipes()

        def __save_recipes(self):
            self.__manager.save_recipes()

        def __exit(self):
            success = self.__manager.save_recipes()
            if not success:
                print("Failed to save recipes!")

            sys.exit(0)

