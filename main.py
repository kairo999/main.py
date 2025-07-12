import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'm your quiz bot 🤖")

app = ApplicationBuilder().token(7691172379:AAFH-jvRpv8lJ5nzbZM4-gE5QrsFc8QsgFQ).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
