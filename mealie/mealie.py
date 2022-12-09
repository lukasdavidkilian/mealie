import random
from food import nutrition_set_lukas
from meal_plan import meal_plan, meal_plans


def mealie(nutrition_set, goals):
    while len(meal_plans) < 3:
        protein_goal = goals[0]
        fat_goal = goals[1]
        carbohydrate_goal = goals[2]

        protein = protein_goal
        fat = fat_goal
        carbohydrate = carbohydrate_goal

        plan_array = []

        for current_food in nutrition_set:
            new_nutrition_set = nutrition_set
            if protein >= -10 and fat >= -5 and carbohydrate >= -10:
                current_food = random.choice(new_nutrition_set)
                random_recommended_amount = random.choice(current_food.recommendedAmounts)
                if current_food not in plan_array:
                    current_food.dailyAmount = random_recommended_amount
                    protein -= current_food.protein * current_food.dailyAmount
                    fat -= current_food.fat * current_food.dailyAmount
                    carbohydrate -= current_food.carbs * current_food.dailyAmount
                    plan_array.append(current_food)
        if -10 <= protein <= 10 and -5 <= fat <= 5 and -10 <= carbohydrate <= 10:
            meal_plan(plan_array, goals[0], goals[1], goals[2])
    return meal_plans

mealie(nutrition_set_lukas, [230, 65, 280])
