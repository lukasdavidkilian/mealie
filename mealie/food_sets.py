from food_class import Food

nutrition_set_all = []
nutrition_set_lukas = []
nutrition_set_daniel = []

nutrition_sets = {
    "lukas": nutrition_set_lukas,
    "daniel": nutrition_set_daniel,
    "all": nutrition_set_all
}

# PROTEIN

rinderhackfleisch = Food("Rinderhackfleisch", 25, 9, 0, 100, "g", [2.5, 3, 3.5, 4])
hähnchenbrust = Food("Hähnchenbrust", 30, 1, 0, 100, "g", [2.5, 3, 3.5, 4])
putenbrust = Food("Putenbrust", 30, 1, 0, 100, "g", [2.5, 3, 3.5, 4])
bauernschinken = Food("Bauernschinken", 26.3, 6.8, 1.1, 100, "g", [0.75, 1])
lachs = Food("Lachs", 20, 13, 0, 100, "g", [1.25, 2.5])
garnelen = Food("Garnelen", 18.6, 1.4, 0, 100, "g", [1.25, 2.5])
eier = Food("Eier", 7.5, 6.5, 1, 1, "", [3, 4, 5,])
milch = Food("Milch", 3.3, 4, 4.8, 100, "ml", [2.5, 3, 3.5, 4])
käse = Food("Käse", 30, 23, 0.1, 100, "g", [0.75, 1])

nutrition_set_all.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, käse])
nutrition_set_lukas.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, eier, milch, käse])
nutrition_set_daniel.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen])

# CARBS

reis = Food("Basmati Reis", 8.8, 1, 75, 100, "g", [0.75, 1])
kartoffeln = Food("Kartoffeln", 2, 0, 17, 100, "g", [4, 5, 6])
süßkartoffeln = Food("Süßkartoffeln", 1.6, 0.6, 24, 100, "g", [4, 5, 6])
buchweizen = Food("Buchweizen", 10, 2, 70, 100, "g", [0.5, 1])
honig = Food("Honig", 0, 0, 80, 100, "g", [0.2, 0.3, 0.4])
banane = Food("Banane", 1.1, 0.3, 22.8, 100, "g", [1, 2])
apfel = Food("Apfel", 0.3, 0.2, 14, 100, "g", [1.5])
heidelbeeren = Food("Heidelbeeren", 0.6, 0.6, 7.4, 100, "g", [1, 1.5, 2])

nutrition_set_all.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_lukas.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_daniel.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])

# Nuts & Seeds

nusskernmischung = Food("Nusskernmischung", 21, 56, 11, 100, "g", [0.3])

nutrition_set_all.extend([nusskernmischung])
nutrition_set_lukas.extend([nusskernmischung])
nutrition_set_daniel.extend([nusskernmischung])

