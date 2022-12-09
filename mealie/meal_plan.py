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
        for i in range(len(self.food)):
            food = self.food[i]
            dailyAmount = food.amount * food.dailyAmount
            foodStr = str(int(dailyAmount)) + " " + food.unit + " " + food.name + " "

            self.protein = self.protein + round(food.protein * food.dailyAmount)
            self.fat = self.fat + round(food.fat * food.dailyAmount)
            self.carbs = self.carbs + round(food.carbs * food.dailyAmount)

            print(foodStr)

            macroStr = "SOLL: P " + str(self.proteinGoal) + "g F " + str(self.fatGoal) + "g C " + \
                       str(self.carbsGoal) + "g\n" + "IST:  P " + str(self.protein) + "g F " + \
                       str(self.fat) + "g C " + str(self.carbs) + "g"

        return("\n" + macroStr + "\n")


