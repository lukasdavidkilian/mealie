from generate_meal_plans import generate_meal_plans
from food_sets import nutrition_set_lukas


# incluce a array for daily amount and save it for meal_plans so the saved amount is in the meal_plan and not in food

def generate_shopping_list(number_of_days, nutrition_set, goal):
    shopping_list = {}
    meal_plans = []

    # Generate the meal plans
    for i in range(number_of_days):
        meal_plans.append(generate_meal_plans(nutrition_set, goal))

    # Generate the shopping list
    for meal_plan in meal_plans:
        for food in meal_plan.food:
            if food.name in shopping_list:
                shopping_list[food.name] += meal_plan.amounts_dictionary[food] * food.amount
            else:
                shopping_list[food.name] = meal_plan.amounts_dictionary[food] * food.amount

    # Calculate the maximum length of the food names
    # (to determine the width of the columns in the table)
    max_name_length = max(len(name) for name in shopping_list)

    # Initialize a string for the shopping list
    shopping_list_str = ""

    # Loop over the items in the shopping list
    for name, amount in shopping_list.items():
        # Find the unit of the current food
        for meal_plan in meal_plans:
            for food in meal_plan.food:
                if food.name == name:
                    unit = food.unit
                    break
        # Format the item and its amount as a row in the table
        shopping_list_str += f"{amount:>5.0f} {unit:>2} {name:<{max_name_length}}\n"

    # Return the shopping list and the meal plans as a tuple
    return shopping_list_str, meal_plans
