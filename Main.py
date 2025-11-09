# Created by Kyle Parker and Koa Hawn
# COMP 3005 Python
# Autumn 2025
#
# Due Nov 14, 2025 @ 19:00

import Logic # Usage: Logic.func name
from IoManager import IoManager # Usage: IoManager.method
from RecipeManager import RecipeManager # Usage: RecipeManager().method

def main():
    input_str = IoManager.get_str("What is your name?")
    input_str_non_empty = IoManager.get_str("What is your City?", empty_ok=False)

    print(f"Your name is {input_str}\nYour city is {input_str_non_empty}.")

if __name__ == "__main__":
    main()
