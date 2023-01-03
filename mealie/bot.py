import re
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater
from generate_meal_plans import generate_meal_plans
from food_sets import nutrition_sets
from meal_plan import meal_plans
from generate_shopping_list import generate_shopping_list
import json
from telegram import Document

# Dictionary to store the macronutrient goals
goals = [0, 0, 0]


def mealie(update, context):
    # Call the mealie function and store the result in a variable
    for i in range(3):
        result = generate_meal_plans(context.user_data["nutrition_set"], goals)
        # Use the __str__ method to convert the result to a string
        result_str = ""
        result_str += result.__str__() + "\n"
        update.message.reply_text(result_str)





def set_nutrition_set(update, context):
    # Split the message into words and lowercase the set name
    set_name = update.message.text.split()[1].lower()
    # Check if the set name is in the nutrition_sets dictionary
    if set_name in nutrition_sets:
        # Set the user's nutrition set to the specified set
        context.user_data["nutrition_set"] = nutrition_sets[set_name]
        update.message.reply_text(f"Dein Nährstoffset wurde auf '{set_name}' gesetzt.")
    else:
        update.message.reply_text(f"Es gibt kein Nährstoffset mit dem Namen '{set_name}'.")


def generate_shopping_list_command(update, context):
    # Get the number of days from the command
    match = re.search(r"\d+", update.message.text)
    if match:
        number_of_days = int(match.group())
    else:
        update.message.reply_text("Please specify the number of days for which you want to generate a shopping list.")
        return

    # Generate the shopping list and meal plans
    shopping_list_str, meal_plans = generate_shopping_list(number_of_days, context.user_data["nutrition_set"], goals)

    # Send the shopping list and meal plans to the user
    update.message.reply_text(shopping_list_str)
    for meal_plan in meal_plans:
        update.message.reply_text(meal_plan.__str__())


def protein(update, context):
    # Extract the number from the command using a regular expression
    match = re.search(r"\d+", update.message.text)
    if match:
        amount = int(match.group())
        if amount > 400:
            amount = 400
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

def starten(update, context):
    # Open the PDF file and get its file object
    with open("/Users/lukaskilian/PycharmProjects/mealie/mealie/Mealie_Help_Command.pdf", "rb") as f:
        # Use the send_document method to send the file to the user
        context.bot.send_document(chat_id=update.effective_chat.id, document=f)

def save_message(update, context):
    # Get the message and chat_id from the update
    message = update.message
    chat_id = message.chat_id
    # Save the message and chat_id to a file
    with open("messages.txt", "a") as f:
        f.write(f"{chat_id}: {message.text}\n")



updater = Updater("5838155917:AAGWYB3CcnMmYCuQiyl2gFghU1JOgcVQJog", use_context=True)

updater.dispatcher.add_handler(CommandHandler("mealie", mealie))
updater.dispatcher.add_handler(CommandHandler("p", protein))
updater.dispatcher.add_handler(CommandHandler("k", carbohydrate))
updater.dispatcher.add_handler(CommandHandler("f", fat))
updater.dispatcher.add_handler(CommandHandler("ziele", ziele))
updater.dispatcher.add_handler(CommandHandler("hilfe", hilfe))
updater.dispatcher.add_handler(CommandHandler("set", set_nutrition_set))
updater.dispatcher.add_handler(CommandHandler("einkaufen", generate_shopping_list_command))
updater.dispatcher.add_handler(CommandHandler("starten", starten))
# Create a MessageHandler to handle all incoming messages
message_handler = MessageHandler(Filters.all, save_message)
updater.dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()
