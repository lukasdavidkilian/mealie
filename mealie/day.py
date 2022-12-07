days = []

class Day:
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
        ausgabe(self)
        days.append(self)


def ausgabe(Day):
    macroStr = ""
    for i in range(len(Day.food)):
        food = Day.food[i]
        dailyAmount = food.amount * food.dailyAmount
        foodStr = str(int(dailyAmount)) + " " + food.unit + " " + food.name + " "

        Day.protein = Day.protein + round(food.protein * food.dailyAmount)
        Day.fat = Day.fat + round(food.fat * food.dailyAmount)
        Day.carbs = Day.carbs + round(food.carbs * food.dailyAmount)

        print(foodStr)

        macroStr = "SOLL: P " + str(Day.proteinGoal) + "g F " + str(Day.fatGoal) + "g C " + \
                   str(Day.carbsGoal) + "g\n" + "IST:  P " + str(Day.protein) + "g F " + \
                   str(Day.fat) + "g C " + str(Day.carbs) + "g"

    print("\n" + macroStr + "\n")
