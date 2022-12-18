import re
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from generate_meal_plans import generate_meal_plans
from food_sets import nutrition_set_lukas
from meal_plan import meal_plans
import json

# Dictionary to store the macronutrient goals
goals = [0,0,0]

def mealie(update, context):
        # Call the mealie function and store the result in a variable
    for i in range(3):
        result = generate_meal_plans(nutrition_set_lukas, goals)
        # Use the __str__ method to convert the result to a string
        result_str = ""
        result_str += result.__str__() + "\n"
        update.message.reply_text(result_str)

def protein(update, context):
    # Extract the number from the command using a regular expression
    match = re.search(r"\d+", update.message.text)
    if match:
        amount = int(match.group())
        goals[0] = amount
        update.message.reply_text(f"Dein Proteinziel ist {amount}g.")
    else:
        update.message.reply_text("Bitte gib dein Proteinziel ein.")

def carbohydrate(update, context):
    # Extract the number from the command using a regular expression
    match = re.search(r"\d+", update.message.text)
    if match:
        amount = int(match.group())
        goals[2] = amount
        update.message.reply_text(f"Dein Kohlenhydratziel ist {amount}g.")
    else:
        update.message.reply_text("Bitte gib dein Kohlenhydratziel ein.")

def fat(update, context):
    # Extract the number from the command using a regular expression
    match = re.search(r"\d+", update.message.text)
    if match:
        amount = int(match.group())
        goals[1] = amount
        update.message.reply_text(f"Dein Fettziel ist {amount}g.")
    else:
        update.message.reply_text("Bitte gib dein Fettziel ein..")

def ziele(update, context):
    reply = f"Your goals are:\n"
    reply += f"- Protein: {goals[0]} grams\n"
    reply += f"- Carbohydrates: {goals[2]} grams\n"
    reply += f"- Fat: {goals[1]} grams\n"
    update.message.reply_text(reply)

def hilfe(update, context):
    reply = "Ich bin ein Telegram-Bot, der dir beim Planen deiner Mahlzeiten hilft.\n\n"
    reply += "Folgende Befehle stehen zur Verfügung:\n"
    reply += "/mealie - Generiert Mahlzeitenpläne basierend auf deinen Makronährstoffzielen.\n"
    reply += "/p - Setzt dein Proteinziel in Gramm. Beispiel: '/p 180' setzt das Ziel auf 180g Protein pro Tag.\n"
    reply += "/k - Setzt dein Kohlenhydratziel in Gramm. Beispiel: '/k 240' setzt das Ziel auf 240g Kohlenhydrate pro Tag.\n"
    reply += "/f - Setzt dein Fettziel in Gramm. Beispiel: '/f 80' setzt das Ziel auf 80g Fett pro Tag.\n"
    reply += "/ziele - Zeigt deine aktuellen Makronährstoffziele an.\n"
    reply += "/hilfe - Zeigt diese Hilfe an.\n"
    update.message.reply_text(reply)

updater = Updater("5800016260:AAFkVxLjJoGSFmpdHPzAPRw_r0gl3Z9TdPU", use_context=True)

updater.dispatcher.add_handler(CommandHandler("mealie", mealie))
updater.dispatcher.add_handler(CommandHandler("p", protein))
updater.dispatcher.add_handler(CommandHandler("k", carbohydrate))
updater.dispatcher.add_handler(CommandHandler("f", fat))
updater.dispatcher.add_handler(CommandHandler("ziele", ziele))
updater.dispatcher.add_handler(CommandHandler("hilfe", hilfe))

updater.start_polling()
updater.idle()