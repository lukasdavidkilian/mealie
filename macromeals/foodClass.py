class Food:
    name = "Lebensmittel"
    calories = "Kalorien"
    fat = "Fett"
    protein = "Protein"
    carbs = "Kohlenhydrate"
    amount = "Menge"
    unit = "Einheit"
    recommendedAmounts = "Empfohlene Menge"
    dailyAmount = "Täglicher Bedarf"

    def __init__(self, name, protein, fat, carbs, amount, unit, recommendedAmounts):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.amount = amount
        self.unit = unit
        self.recommendedAmounts = recommendedAmounts

def ausgabe(Food):
    str = 'In {amount}{unit} {name} sind {protein}g Protein, {fat}g Fett und {carbs}g Kohlenhydrate. '.format(
        amount=Food.amount, unit=Food.unit, name=Food.name, protein=Food.protein,
        fat=Food.fat, carbs=Food.carbs)
    print(str)

    '''


        def print(self):
            """Beispielmethode"""
            print(f"Name: {self.name}\nCalories: {self.calories}\nFat: {self.fat}%")
            '''