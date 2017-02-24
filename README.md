# Shopping-List Creator
A tool that transforms a meal plan with ingredients for all days of the week into a shopping list with amounts to buy.
Customized to the way you eat.
Zero waste.

# Use
1.  Download groceries.py
2.  Do `python groceries.py` with the required files (listed below) in the same folder as groceries.py

# Required Files
`groceries.py` needs the following two files in its folder to run:
*   a `meal_plan.xlsx` file containing a grid with the names of ingredients for your meals;
*   a `dictionary.csv` file containing all ingredients from which you could choose to make your meals, the measuring units in which you count every ingredient at the moment of shopping (e.g. unit, lb., gr., handful, tbs...), the amounts that you use for each meal (consider your measuring units), and rules to purchase these ingredients (color, shape, consistency, etc.)

The output is a .txt file called "shopping list".
