# main.py

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Define /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hello! I'm your AI Assistant Bot. Type /help to see what I can do.")

# Define /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = (
        "🤖 *Available Commands:*\n"
        "/ask [question] — Ask me anything\n"
        "/summarize [URL] — Summarize web articles\n"
        "/remind [text] at [time] — Set a reminder\n"
        "/history — Show recent interactions\n"
        "/help — Show this help message"
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

# Run the bot
if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("✅ Bot is running...")
    app.run_polling()
