from food_sets import nutrition_set_lukas
from generate_meal_plans import generate_meal_plans
from generate_shopping_list import generate_shopping_list
from meal_plan import meal_plans

protein_goal = 230
fat_goal = 65
carbohydrate_goal = 280

goal = [protein_goal, fat_goal, carbohydrate_goal]


shopping_list = generate_shopping_list(3,nutrition_set_lukas,goal)
print(shopping_list)