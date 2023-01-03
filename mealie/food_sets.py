from food_class import Food

nutrition_set_all = []
nutrition_set_lukas = []
nutrition_set_daniel = []
nutrition_set_lucas = []
nutrition_set_rico = []


nutrition_sets = {
    "lukas": nutrition_set_lukas,
    "daniel": nutrition_set_daniel,
    "all": nutrition_set_all,
    "lucas": nutrition_set_lucas,
    "rico": nutrition_set_rico
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
roteLinsen = Food("Rote Linsen", 26.7, 1.5, 57.8, 100, "g", [1, 2, 3])
kichererbsen = Food("Kichererbsen", 20, 7, 45, 100, "g", [1, 2, 3])
kidneybohnen = Food("Kidneybohnen", 21, 1, 36.5, 100, "g", [0.75, 1])

nutrition_set_all.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, käse])
nutrition_set_lukas.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, eier, milch, käse])
nutrition_set_daniel.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen])
nutrition_set_lucas.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, käse])
nutrition_set_rico.extend([rinderhackfleisch, hähnchenbrust, putenbrust, bauernschinken, lachs, garnelen, eier, milch, käse])



# CARBS

reis = Food("Basmati Reis", 8.8, 1, 75, 100, "g", [0.75, 1])
kartoffeln = Food("Kartoffeln", 2, 0, 17, 100, "g", [4, 5, 6])
süßkartoffeln = Food("Süßkartoffeln", 1.6, 0.6, 24, 100, "g", [4, 5, 6])
buchweizen = Food("Buchweizen", 10, 2, 70, 100, "g", [0.5, 1])
honig = Food("Honig", 0, 0, 80, 100, "g", [0.2, 0.3, 0.4])
banane = Food("Banane", 1.1, 0.3, 22.8, 100, "g", [1, 2])
apfel = Food("Apfel", 0.3, 0.2, 14, 100, "g", [1.5])
heidelbeeren = Food("Heidelbeeren", 0.6, 0.6, 7.4, 100, "g", [1, 1.5, 2])
mango = Food("Mango", 2, 0.2, 13, 100, "g", [1, 1.5, 2])
reiswaffeln = Food("Reiswaffeln", 8, 3.6, 80.2, 100, "g", [0.15, 0.3, 0.45])
spinat = Food("Spinat", 2.8, 0.3, 0.6, 100, "g", [1, 1.5, 2])
blumenkohl = Food("Blumenkohl", 1.9, 0, 2, 100, "g", [1, 1.5, 2])
paprikarot = Food("Rote Paprika", 1.3, 0.5, 6.4, 100, "g", [1, 2, 3])
paprikagelb = Food("Gelbe Paprika", 1, 0, 5, 100, "g", [1, 2, 3])
paprikagrün = Food("Grüne Paprika", 1, 0, 2, 100, "g", [1, 2, 3])
karotte = Food("Karotte", 1, 0.2, 4.8, 100, "g", [1, 2, 3])
tomate = Food("Tomate", 0.7, 3.5, 0.1, 100, "g", [1, 2, 3])
gurke = Food("Gurke", 0.6, 0.2, 1.8, 100, "g", [1, 2, 3])
beerenmischung = Food("Beerenmischung TK", 1.4, 0.6, 12.1, 100, "g", [0.5, 1, 1.5])
mandarine = Food("Mandarine", 0.7, 0.2, 10, 100, "g", [1, 2, 3])
orange = Food("Orange", 1, 0.2, 8.2, 100, "g", [1, 2, 3])
birne = Food("Mandarine", 1, 0.2, 11, 100, "g", [1, 2, 3])
ananas = Food("Ananas", 0.5, 0.2, 12.4, 100, "g", [1, 2, 3])
dattel = Food("Dattel getrocknet", 1.85, 0.5, 65, 100, "g", [0.1, 0.2, 0.3])
ketchup = Food("Ketchup", 2, 0.3, 24, 100, "g", [0.15, 0.3])
sriracha = Food("Sriracha", 1.8, 1.3, 23, 100, "g", [0.15, 0.3])
sojasauce = Food("Sojasauce glutenfrei", 10, 0, 2, 100, "g", [0.2, 0.4])
gehackteTomaten = Food("Tomaten gehackt", 1.1, 0.1, 3, 100, "g", [2, 3, 4])
grüneBohnen = Food("Grüne Bohnen", 2.4, 0, 5, 100, "g", [1, 2])
raeuchertofu = Food("Räuchertofu", 19, 9, 2.8, 100, "g", [1, 2])


nutrition_set_all.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_lukas.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_daniel.extend([reis, kartoffeln, süßkartoffeln, buchweizen, honig, banane, apfel])
nutrition_set_lucas.extend([reis, kartoffeln, süßkartoffeln, honig, banane, apfel])
nutrition_set_rico.extend([reis, kartoffeln, honig, banane, apfel])
#nutrition_set_rico.remove(buchweizen)
#nutrition_set_rico.remove(süßkartoffeln)

# FAT

nusskernmischung = Food("Nusskernmischung", 21, 56, 11, 100, "g", [0.3])
walnüsse = Food("Walnüsse", 16, 71, 6, 100, "g", [0.3])
olivenoel = Food("Olivenöl", 0, 100, 0.2, 100, "g", [0.15, 0.3, 0.45])
butterschmalz = Food("Butterschmalz", 0.3, 100, 0, 100, "g", [0.3])
hummus = Food("Hummus", 7.9, 9.6, 14.3, 100, "g", [0.25, 0.5, 0.75])

nutrition_set_all.extend([nusskernmischung])
nutrition_set_lukas.extend([nusskernmischung])
nutrition_set_daniel.extend([nusskernmischung])
nutrition_set_lucas.extend([nusskernmischung])
nutrition_set_rico.extend([nusskernmischung])

