from food_sets import nutrition_set_lukas
from mealie import mealie

protein_goal = 230
fat_goal = 65
carbohydrate_goal = 280

goal = [protein_goal, fat_goal, carbohydrate_goal]

mealie(nutrition_set_lukas, goal)
