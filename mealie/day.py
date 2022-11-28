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
        foodStr = "{amount} {unit} {name} ".format(amount=int(dailyAmount), name=food.name,
                                                  unit=food.unit)

        Day.protein = Day.protein + round(food.protein * food.dailyAmount)
        Day.fat = Day.fat + round(food.fat * food.dailyAmount)
        Day.carbs = Day.carbs + round(food.carbs * food.dailyAmount)


        print(foodStr)

        macroStr = "SOLL: P {proteinGoal}g F {fatGoal}g C {carbsGoal}g\n" \
                    "IST:  P {protein}g F {fat}g C {carbs}g".format(proteinGoal= Day.proteinGoal,
                                                                                    protein= Day.protein,
                                                                                    fatGoal= Day.fatGoal, fat= Day.fat,
                                                                                    carbsGoal= Day.carbsGoal,
                                                                                    carbs=  Day.carbs
                                                                                    )
    print("")
    print(macroStr)
    print("")
