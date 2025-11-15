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
            with open("recipes.psv", "r") as file:
                lines = file.readlines()[1:] # Skip header
                recipes = [RecipeFactory.create_from_psv_line(line) for line in lines]

        except FileNotFoundError:
            print("Recipes.psv not found")
        except IOError:
            print("Recipes.psv is not available! (Check permissions)")
        except RecipeMalformedError:
            print("Input recipe list was malformed! No data could be read!")
        except:
            print("Something went wrong while reading recipes.csv. :(")

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

    def __search_for_recipe(self, name, partial=False):
        # TODO: Use linear search
        # TODO: If there is time, use binary search
        # Search for recipe, by name
        if not name:
            return -1
        target = name.strip().lower()
        for i, recipe in enumerate(self.__recipes):
            try:
                recipe_name = recipe.name().lower()
                if partial:
                    if target in recipe_name:
                        return i
                else:
                    if target == recipe_name:
                        return i
            except (AttributeError, TypeError) as e:
                print(f"Error processing recipe: {e}")
                continue
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
        n = len(self.__recipes)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                try:
                    current_recipe_name = str(getattr(self.__recipes[j], 'name', '')).lower()
                    next_recipe_name = str(getattr(self.__recipes[j + 1], 'name', '')).lower()

                    if current_recipe_name > next_recipe_name:
                        self.__recipes[j], self.__recipes[j + 1] = self.__recipes[j + 1], self.__recipes[j]
                        swapped = True
                except (AttributeError, TypeError) as e:
                    print(f"Error comparing recipe names: {e}")
                    continue
            if not swapped:
                break

    def __sort_recipes_by_date(self):
        # TODO: Use bubble sort, based off date created
        n = len(self.__recipes)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                try:
                    current_date = getattr(self.__recipes[j], 'date_created', None)
                    next_date = getattr(self.__recipes[j + 1], 'date_created', None)

                    if current_date is None and next_date is not None:
                        self.__recipes[j], self.__recipes[j + 1] = self.__recipes[j + 1], self.__recipes[j]
                        swapped = True
                    elif (current_date is not None and next_date is not None and
                          current_date > next_date):
                        self.__recipes[j], self.__recipes[j + 1] = self.__recipes[j + 1], self.__recipes[j]
                        swapped = True
                except (AttributeError, TypeError) as e:
                    print(f"Error comparing recipe dates: {e}")
                    continue
            if not swapped:
                break

    def __sort_recipes_by_rating(self):
        # TODO: Use bubble sort, based off rating
        # see __sort_recipes_by_time for bubble sort, or use a more efficient alg
        n = len(self.__recipes)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                try:
                    current_rating = getattr(self.__recipes[j], 'rating', 0)
                    next_rating = getattr(self.__recipes[j + 1], 'rating', 0)

                    if current_rating is None:
                        current_rating = 0
                    if next_rating is None:
                        next_rating = 0
                    current_rating = float(current_rating)
                    next_rating = float(next_rating)
                    if current_rating < next_rating:
                        self.__recipes[j], self.__recipes[j + 1] = self.__recipes[j + 1], self.__recipes[j]
                        swapped = True
                except (ValueError, TypeError) as e:
                    print(f"Error comparing recipe ratings: {e}")
                    continue
            if not swapped:
                break
        print(f"Recipes sorted by rating. Total recipes: {n}")

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
            print("\nRecipe Search Options:")
            print("1. Search by Full Recipe Name")
            print("2. Search by Partial Recipe Name")
            print("3. Cancel Search")
            try:
                choice = int(input("Enter your choice (1-3): "))
                if choice == 1:
                    name = input("Enter the exact recipe name: ").strip()
                    index = self.__search_for_recipe(name, partial=False)

                    if index != -1:
                        print("\nRecipe Found:")
                        print(self.__recipes[index])
                    else:
                        print(f"No recipe found with the exact name '{name}'.")
                elif choice == 2:
                    name = input("Enter part of the recipe name: ").strip()
                    index = self.__search_for_recipe(name, partial=True)
                    if index != -1:
                        print("\nRecipe Found:")
                        print(self.__recipes[index])
                    else:
                        print(f"No recipe found containing '{name}'.")
                elif choice == 3:
                    print("Search cancelled.")
                    return None
                else:
                    print("Invalid choice. Please select 1, 2, or 3.")

            except ValueError:
                print("Please enter a valid number.")
            except Exception as e:
                print(f"An error occurred during search: {e}")

    @property
    def add_recipe(self):
        # TODO: Implement add_recipe
        # Prompt for each field, then use RecipeFactory to generate a recipe object and save add it to the list
        try:
            # Recipe Name Input
            name = input("Enter Recipe Name: ").strip()

            # Chef Name Input
            chef = input("Enter Chef's Name: ").strip()

            # Ingredients Input
            ingredients = []
            print("\nIngredient Input")
            # [Similar logic to previous implementation]

            # Tools Input
            tools = []
            print("\nTools Needed")
            # [Similar logic to previous implementation]

            # Rating Input
            rating = float(input("Enter recipe rating (0-5): "))

            # Create Recipe using RecipeFactory
            new_recipe = RecipeFactory.create(
                name=name,
                chef=chef,
                ingredients=ingredients,
                tools=tools,
                rating=rating,
                # Use predefined time objects as in the original code
                cooking_time=time(0, 30),  # Default 30 minutes
                prep_time=time(0, 20),  # Default 20 minutes
                total_time=time(0, 50)  # Default 50 minutes
            )

            # Add recipe to the list
            self.__recipes.append(new_recipe)

            # Confirmation
            print("\n--- Recipe Added Successfully ---")
            print(new_recipe)

            return new_recipe

        except Exception as e:
            print(f"An error occurred while adding the recipe: {e}")
            return None

    def remove_recipe(self):
        # TODO: Implement remove_recipe()
        # List all items with a for or while loop
        # Check if there are any recipes
        if not self.__recipes:
            print("No recipes available to remove.")
            return None

        # Display all recipes with index numbers
        print("\n--- CURRENT RECIPES ---")
        for index, recipe in enumerate(self.__recipes, 1):
            print(f"{index}. {recipe.name} (by {recipe.chef})")

        # Recipe removal process
        while True:
            try:
                # Prompt for recipe selection
                choice = input("\nEnter the number of the recipe to remove (or '0' to cancel): ").strip()

                # Cancel option
                if choice == '0':
                    print("Recipe removal cancelled.")
                    return None

                # Convert choice to integer index
                index = int(choice) - 1

                # Validate index
                if 0 <= index < len(self.__recipes):
                    # Confirm removal
                    recipe_to_remove = self.__recipes[index]
                    confirm = input(f"Are you sure you want to remove '{recipe_to_remove.name}'? (yes/no): ").lower()

                    if confirm in ['yes', 'y']:
                        # Remove the recipe
                        removed_recipe = self.__recipes.pop(index)

                        print(f"\n--- RECIPE REMOVED ---")
                        print(f"Removed: {removed_recipe.name}")

                        # Optional: Immediate save
                        save_choice = input("Do you want to save changes? (yes/no): ").lower()
                        if save_choice in ['yes', 'y']:
                            self.save_recipes()
                            print("Recipes saved successfully!")

                        return removed_recipe
                    else:
                        print("Recipe removal cancelled.")
                        return None

                else:
                    print("Invalid recipe number. Please try again.")

            except ValueError:
                print("Please enter a valid number.")

            except Exception as e:
                print(f"An unexpected error occurred: {e}")

    def edit_recipe(self):
        # TODO: Implement edit_recipe
        # Use menu object as in Application
        # Check if there are recipes to edit
        if not self.__recipes:
            print("No recipes available to edit.")
            return False

        # Display all recipes
        print("\n--- RECIPE LIST ---")
        for i, recipe in enumerate(self.__recipes, 1):
            print(f"{i}. {recipe.name} (by {recipe.chef})")

        try:
            # Get recipe selection
            choice = int(input("\nEnter the number of the recipe to edit (or 0 to cancel): "))

            # Cancel option
            if choice == 0:
                print("Recipe editing cancelled.")
                return False

            # Validate recipe index
            if 1 <= choice <= len(self.__recipes):
                recipe = self.__recipes[choice - 1]

                # Placeholder for future implementation
                # This matches the minimal approach in the Application class
                print(f"Editing recipe: {recipe.name}")
                # TODO: Implement actual editing logic

                return True
            else:
                print("Invalid recipe number.")
                return False

        except ValueError:
            print("Please enter a valid number.")
            return False

    def sort_recipes(self):
        # TODO: Implement sort_recipes
        # Prompt to see how to sort. Then call one of the functions above. Use Menu object! See Application.py for example. Ask AI if you are unsure.
        # Define sorting options
        sort_menu = {
            "Sort by Name": self.__sort_recipes_by_name,
            "Sort by Rating": self.__sort_recipes_by_rating,
            "Sort by Cooking Time": self.__sort_recipes_by_time,
            "Sort by Date Created": self.__sort_recipes_by_date
        }

        while True:
            # Display sorting options
            print("\n--- SORT RECIPES ---")
            for i, option in enumerate(sort_menu.keys(), 1):
                print(f"{i}. {option}")
            print(f"{len(sort_menu) + 1}. Cancel")

            try:
                # Get user choice
                choice = int(input("\nEnter your choice (1-{len(sort_menu) + 1}): "))

                # Cancel option
                if choice == len(sort_menu) + 1:
                    print("Sorting cancelled.")
                    break

                # Validate and execute choice
                if 1 <= choice <= len(sort_menu):
                    # Get the corresponding method for the selected option
                    sort_method = list(sort_menu.values())[choice - 1]

                    # Execute the sorting method
                    sort_method()
                    print("Recipes sorted successfully.")
                    break
                else:
                    print("Invalid choice. Please try again.")

            except ValueError:
                print("Please enter a valid number.")

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