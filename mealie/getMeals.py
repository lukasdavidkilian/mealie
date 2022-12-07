from random import random
from food import foodList, lukas, daniel
from day import Day

def getMeals(foodArray, goals):

    proteinGoal = goals[0]
    fatGoal = goals[1]
    carbsGoal = goals[2]

    protein = proteinGoal
    fat = fatGoal
    carbs = carbsGoal

    emptyArray = []
    for i in range(len(foodArray)):
        newFoodArray = foodArray
        if(protein >= -10 and fat >= -5 and carbs >= -10):
            zahl = int(random() * len(newFoodArray))
            food = newFoodArray[zahl]
            randomRecommendedAmount = int(random() * len(food.recommendedAmounts))
            if(food not in emptyArray):
                food.dailyAmount = food.recommendedAmounts[randomRecommendedAmount]
                protein = protein - food.protein * food.dailyAmount
                fat = fat - food.fat * food.dailyAmount
                carbs = carbs - food.carbs * food.dailyAmount
                emptyArray.append(food)
    if(protein >= -10 and protein <= 10 and fat >= -5 and fat <= 5 and carbs >= -10 and carbs <= 10):
        Day(emptyArray, goals[0], goals[1], goals[2])

goals = [150,70,250]

def mealie(foodArray, goals):
    for t in range(100000):
        getMeals(foodArray, goals)

mealie(lukas, goals)