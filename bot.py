import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Yahan apna BotFather se mila hua Token dalein
TOKEN = "YOUR_BOT_TOKEN_HERE"

# Yeh aapka GitHub Pages ka link hai jo abhi banaya hai
WEB_APP_URL = "https://akashgurjar1202-stack.github.io/my-telegram-webapp/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎨 Open Colorful Menu", web_app_url=WebAppInfo(url=WEB_APP_URL))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Welcome! Click the button below to open your colorful Telegram Mini App:",
        reply_markup=reply_markup
    )

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Jab user WebApp ke andar 'Claim' button dabayega toh ye chalega
    data = update.message.web_app_data.data
    if "claim_reward" in data:
        await update.message.reply_text("🎉 Badhai ho! Aapka reward successfully claim ho gaya hai!")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.StatusUpdate.WEB_APP_DATA, handle_webapp_data))
    
    print("Bot is running...")
    app.run_polling()
