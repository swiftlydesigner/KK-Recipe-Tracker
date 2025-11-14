# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00
from datetime import time

from Ingredient import Ingredient
from Recipe import Recipe
from RecipeFactory import RecipeFactory, RecipeMalformedError


class RecipeManager:
    ''' Attributes:
        - __recipes: list of Recipe objects -> [Recipe]
    '''
    def __init__(self):
        self.__recipes = self.__read_from_psv()

    def __del__(self):
        self.__save_recipes(self.__recipes)

    # MARK: - Private Data Mutators
    @staticmethod
    def __csv(data):
        if isinstance(data, list) or isinstance(data, tuple):
            l = []
            for d in data:
                if isinstance(d, list):
                    l.append(RecipeManager.__csv(d))
                else:
                    l.append(str(d).replace(",", "?")) # Custom storage to avoid collision with ,
            return ",".join(l)
        return data

    def __recipe_to_psv(self, recipe) -> str:
        l = recipe.get_list()
        l = [RecipeManager.__csv(ele) for ele in l]
        return "|".join(str(ele).replace("|", "\\|") for ele in l)

    # MARK: - Private Handlers
    def __read_from_psv(self):
        recipes = []
        try:
            with open("Recipes.psv", "r") as file:
                lines = file.readlines()[1:] # Skip header
                recipes = [RecipeFactory.create_from_psv_line(line) for line in lines]

        except FileNotFoundError:
            print("Recipes.psv not found")
        except IOError:
            print("Recipes.psv is not available! (Check permissions)")
        except RecipeMalformedError:
            print("Input recipe list was malformed! No data could be read!")
        except:
            print("Something went wrong while reading Recipes.csv. :(")

        return recipes
        # TODO: Complete Recipe Factory
        return [
        Recipe(
            name="Classic Beef Stroganoff",
            chef="Gordon Ramsay",
            ingredients=[
                Ingredient("Beef Tenderloin", 1.5, "lbs"),
                Ingredient("Mushrooms", 0.5, "lbs"),
                Ingredient("Sour Cream", 1, "cup"),
                Ingredient("Beef Broth", 1, "cup"),
                ["Onions", "Garlic", "Black Pepper", "Salt"],
                [Ingredient("Butter", 0.25, "cup"), Ingredient("Flour", 2, "tablespoons")]
            ],
            tools=["Large Skillet", "Cutting Board", "Chef's Knife", "Wooden Spoon"],
            rating=4.8,
            cooking_time=time(0, 30),  # 30 minutes
            prep_time=time(0, 20),     # 20 minutes
            total_time=time(0, 50)     # 50 minutes
        ),
        Recipe(
            name="Texas-Style Beef Brisket",
            chef="Aaron Franklin",
            ingredients=[
                Ingredient("Beef Brisket", 10, "lbs"),
                Ingredient("Kosher Salt", 0.25, "cup"),
                Ingredient("Black Pepper", 0.25, "cup"),
                ["Beef Rub", "Paprika", "Garlic Powder"],
                [Ingredient("Butcher's Twine", 1, "roll"), "Optional"]
            ],
            tools=["Smoker", "Meat Thermometer", "Butcher Paper", "Cutting Board"],
            rating=5.0,
            cooking_time=time(12, 0),  # 12 hours
            prep_time=time(1, 0),      # 1 hour
            total_time=time(13, 0)     # 13 hours
        ),
        Recipe(
            name="Bacon-Wrapped Filet Mignon",
            chef="Wolfgang Puck",
            ingredients=[
                Ingredient("Filet Mignon", 2, "pieces"),
                Ingredient("Bacon", 4, "slices"),
                Ingredient("Butter", 0.25, "cup"),
                ["Rosemary", "Thyme", "Garlic"],
                [Ingredient("Sea Salt", 2, "teaspoons"), Ingredient("Black Pepper", 1, "teaspoon")]
            ],
            tools=["Cast Iron Skillet", "Meat Thermometer", "Tongs", "Cutting Board"],
            rating=4.9,
            cooking_time=time(0, 15),  # 15 minutes
            prep_time=time(0, 10),     # 10 minutes
            total_time=time(0, 25)     # 25 minutes
        ),
            Recipe(
                name="Hearty Beef Chili",
                chef="Guy Fieri",
                ingredients=[
                    Ingredient("Ground Beef", 2, "lbs"),
                    Ingredient("Kidney Beans", 2, "cans"),
                    Ingredient("Tomato Sauce", 1, "can"),
                    Ingredient("Beef Broth", 1, "cup"),
                    ["Chili Powder", "Cumin", "Garlic", "Onion"],
                    [Ingredient("Cayenne Pepper", 1, "teaspoon"), "Optional Heat"]
                ],
                tools=["Large Pot", "Wooden Spoon", "Cutting Board", "Knife"],
                rating=4.6,
                cooking_time=time(1, 30),  # 1 hour 30 minutes
                prep_time=time(0, 20),  # 20 minutes
                total_time=time(1, 50)  # 1 hour 50 minutes
            ),
            Recipe(
                name="Slow Cooker Pulled Pork",
                chef="Bobby Flay",
                ingredients=[
                    Ingredient("Pork Shoulder", 4, "lbs"),
                    Ingredient("BBQ Sauce", 1, "cup"),
                    Ingredient("Apple Cider Vinegar", 0.25, "cup"),
                    ["Brown Sugar", "Paprika", "Garlic Powder"],
                    [Ingredient("Salt", 2, "tablespoons"), Ingredient("Black Pepper", 1, "tablespoon")]
                ],
                tools=["Slow Cooker", "Meat Shredder", "Cutting Board"],
                rating=4.7,
                cooking_time=time(8, 0),  # 8 hours
                prep_time=time(0, 15),  # 15 minutes
                total_time=time(8, 15)  # 8 hours 15 minutes
            ),
            Recipe(
                name="Classic Beef Lasagna",
                chef="Emeril Lagasse",
                ingredients=[
                    Ingredient("Ground Beef", 1.5, "lbs"),
                    Ingredient("Lasagna Noodles", 1, "box"),
                    Ingredient("Ricotta Cheese", 15, "oz"),
                    Ingredient("Mozzarella Cheese", 2, "cups"),
                    ["Tomato Sauce", "Basil", "Oregano"],
                    [Ingredient("Parmesan Cheese", 0.5, "cup"), "Optional Topping"]
                ],
                tools=["Lasagna Pan", "Skillet", "Mixing Bowl", "Cheese Grater"],
                rating=4.8,
                cooking_time=time(1, 0),  # 1 hour
                prep_time=time(0, 30),  # 30 minutes
                total_time=time(1, 30)  # 1 hour 30 minutes
            )
        ]

    def __save_recipes(self, recipes):
        success = False
        try:
            with open("recipes.psv", "w") as file:
                header = "Name", "Chef", "Ingredients", "Tools", "Rating", "Cooking Time", "Prep Time", "Total Time", "Date"
                file.write("|".join(header) + "\n")
                for recipe in recipes:
                    psv = self.__recipe_to_psv(recipe) + "\n"
                    file.write(psv)

            success = True
        except IOError:
            print("Unable to write recipes!")
        except NameError:
            print("Warning! Fatal internal error!")

        return success

    def __search_for_recipe(self, name):
        # TODO: Use linear search
        # TODO: If there is time, use binary search
        # Search for recipe, by name
        if not name:
            return -1
        target = name.strip().lower()
        for i, r in enumerate(self.__recipes):
            rname = getattr(r, "name", "")
            if not isinstance(rname, str):
                continue
            rname_l = rname.lower()
            if (partial and target in rname_l) or (not partial and rname_l == target):
                return i
        return -1


    def __sort_recipes_by_time(self):
        for i in range(len(self.__recipes)):
            for j in range(i, len(self.__recipes)):
                if self.__recipes[i].total_time() > self.__recipes[j].total_time():
                    tmp = self.__recipes[i]
                    self.__recipes[i] = self.__recipes[j]
                    self.__recipes[j] = tmp

    def __sort_recipes_by_name(self):
        # TODO: Use bubble sort, based off name of recipe
        # see __sort_recipes_by_time for bubble sort, or use a more efficient alg
        pass

    def __sort_recipes_by_date(self):
        # TODO: Use bubble sort, based off date created
        # see __sort_recipes_by_time for bubble sort, or use a more efficient alg
        pass

    def __sort_recipes_by_rating(self):
        # TODO: Use bubble sort, based off rating
        # see __sort_recipes_by_time for bubble sort, or use a more efficient alg
        pass

    # Display all recipes.
    def display_all(self):
        i = 0
        while i < len(self.__recipes):
            print(self.__recipes[i])
            i += 1
        pass

    def search_for_recipe(self):
        # TODO: Implement search
        # Search for a recipe based on name. Or extend this to any field. Implement sorting in the private function (see above).
        # I have this public interface since I am used to proper Software Engineering principles.
        # You can create a menu object and call different sort functions as needed (see example of Menu in Application.py)
        pass

    def add_recipe(self):
        # TODO: Implement add_recipe
        # Prompt for each field, then use RecipeFactory to generate a recipe object and save add it to the list
        pass

    def remove_recipe(self):
        # TODO: Implement remove_recipe()
        # List all items with a for or while loop
        pass

    def edit_recipe(self):
        # TODO: Implement edit_recipe
        # Use menu object as in Application
        pass

    def sort_recipes(self):
        # TODO: Implement sort_recipes
        # Prompt to see how to sort. Then call one of the functions above. Use Menu object! See Application.py for example. Ask AI if you are unsure.
        pass

    def recommend_recipe(self):
        # TODO: Implement recommend_recipe
        # Prompt to see if it should rec based on duration, no ingredients, or something else
        pass

    def load_recipes(self) -> bool:
        # TODO: Implement load_recipe
        pass

    def save_recipes(self) -> bool:
        # TODO: Implement save_recipe
        success = False

        try:
            success = self.__save_recipes(self.__recipes)
        except:
            print("Unknown error occurred during save process!")

        return success