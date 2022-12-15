from food_sets import nutrition_set_lukas
from generate_meal_plans import generate_meal_plans

protein_goal = 230
fat_goal = 65
carbohydrate_goal = 280

goal = [protein_goal, fat_goal, carbohydrate_goal]

generate_meal_plans(nutrition_set_lukas, goal)
