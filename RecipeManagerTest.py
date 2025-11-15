import unittest
from datetime import time

from Ingredient import Ingredient
from Recipe import Recipe
from RecipeManager import RecipeManager


class TestRecipeManagerSort(unittest.TestCase):
    def setUp(self):
        self.recipe_list = self.__get_recipe_list()
        self.uut = RecipeManager(self.recipe_list)

    def __get_recipe_list(self):
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
                prep_time=time(0, 20),  # 20 minutes
                total_time=time(0, 50)  # 50 minutes
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
                prep_time=time(1, 0),  # 1 hour
                total_time=time(13, 0)  # 13 hours
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
                prep_time=time(0, 10),  # 10 minutes
                total_time=time(0, 25)  # 25 minutes
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

    def test_exact_match(self):
        expected = 2
        actual = self.uut.search_for_recipe("Bacon-Wrapped Filet Mignon", partial=False)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}.")

    def test_partial_match(self):
        expected = 4
        actual = self.uut.search_for_recipe("Pork", partial=True)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}.")

    def test_no_match(self):
        expected = -1
        actual = self.uut.search_for_recipe("Pizza", partial=False)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}.")

    def test_empty_name_partial(self):
        expected = -1
        actual = self.uut.search_for_recipe("", partial=True)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}.")

    def test_empty_name(self):
        expected = -1
        actual = self.uut.search_for_recipe("", partial=False)
        self.assertEqual(actual, expected, f"Expected {expected}, but got {actual}.")

if __name__ == '__main__':
    unittest.main()
