from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

# Function to calculate dating percentage
def calculate_percentage(name1: str, name2: str) -> int:
    combined_name = name1.lower() + name2.lower()
    score = sum(ord(char) for char in combined_name) % 101
    return score

# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Welcome to the Name Astrology Dating Bot! "
        "Send two names separated by a comma to get their dating percentage. Example: John, Jane"
    )

# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "To use this bot, just type two names separated by a comma, and I'll calculate their dating percentage based on name astrology!"
    )

# Main logic to handle messages
async def calculate(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    if "," not in text:
        await update.message.reply_text(
            "Please provide two names separated by a comma. Example: John, Jane"
        )
        return

    try:
        name1, name2 = map(str.strip, text.split(",", 1))
        percentage = calculate_percentage(name1, name2)
        await update.message.reply_text(
            f"The dating compatibility between {name1} and {name2} is: {percentage}%!"
        )
    except Exception as e:
        await update.message.reply_text("Oops! Something went wrong. Please try again.")

# Main function to set up the bot
def main() -> None:
    # Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your bot's token from BotFather
    token = "7783916101:AAH2wprTAMvUuHPHA12F-vQ9Oj4LBeMnsSk"
    application = Application.builder().token(token).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    # Message handler
    application.add_handler(MessageHandler(fi