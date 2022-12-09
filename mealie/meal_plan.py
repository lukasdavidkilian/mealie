meal_plans = []

class meal_plan:
    food: []
    proteinGoal: int
    fatGoal: int
    carbsGoal: int

    def __init__(self, food, proteinGoal, fatGoal, carbsGoal):
        self.food = food
        self.proteinGoal = proteinGoal
        self.fatGoal = fatGoal
        self.carbsGoal = carbsGoal
        self.protein = 0
        self.fat = 0
        self.carbs = 0
        print(self)
        meal_plans.append(self)

    def __str__(self):
        # Initialize a string for the meal plan
        meal_plan_str = ""

        # Calculate the maximum length of the food names and units
        # (to determine the width of the columns in the table)
        max_name_length = max(len(food.name) for food in self.food)
        max_unit_length = max(len(food.unit) for food in self.food)

        # Loop over the foods in the meal plan
        for food in self.food:
            # Calculate the daily amount of the food
            daily_amount = food.amount * food.dailyAmount

            # Format the food and its daily amount as a row in the table
            meal_plan_str += (
                f"{daily_amount:>5.0f} {food.unit:<{max_unit_length}} "
                f"{food.name:<{max_name_length}}\n"
            )

        # Calculate the total amount of each nutrient in the meal plan
        protein = sum(food.protein * food.dailyAmount for food in self.food)
        fat = sum(food.fat * food.dailyAmount for food in self.food)
        carbs = sum(food.carbs * food.dailyAmount for food in self.food)

        # Format the goals and totals for the macro nutrients
        macro_str = (
            "SOLL: P {:.0f}g F {:.0f}g C {:.0f}g\n"
            " IST: P {:.0f}g F {:.0f}g C {:.0f}g"
        ).format(self.proteinGoal, self.fatGoal, self.carbsGoal, protein, fat, carbs)

        # Return the meal plan string and macro nutrient string
        return f"\n{meal_plan_str}\n{macro_str}\n"
