from food_sets import nutrition_set_lukas, nutrition_set_celina
from generate_meal_plans import generate_meal_plans
from generate_shopping_list import generate_shopping_list
from meal_plan import meal_plans

protein_goal = 150
fat_goal = 85
carbohydrate_goal = 100

goal = [protein_goal, fat_goal, carbohydrate_goal]

plan = generate_meal_plans(nutrition_set_celina, goal)
print(plan)

#shopping_list = generate_shopping_list(3,nutrition_set_celina,goal)
#print(shopping_list)