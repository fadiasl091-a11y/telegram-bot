from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

import os
TOKEN = os.getenv(Use this token to access the HTTP API:
8749069543:AAHfR9w954N-XbTVLjSnmY1IhH2MkPLNe0EA)

keyboard = [
    ["💰 شراء", "📊 الأسعار"],
    ["📞 تواصل"]
]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "مرحبا بك 👋",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text == "💰 شراء":
        await update.message.reply_text("ارسل الكمية")
    elif update.message.text == "📊 الأسعار":
        await update.message.reply_text("1000 = 1$")
    elif update.message.text == "📞 تواصل":
        await update.message.reply_text("@username")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT, handle))
app.run_polling()
