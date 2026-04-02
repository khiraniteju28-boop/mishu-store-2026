import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, MessageHandler, filters, ContextTypes

# Token aur Voice ID
TOKEN = "8707304999:AAG5ri9VfBLEic1HTyMW4khjfVmLdOpr-Mw"
VOICE_ID = "CQACAgUAAxkBAAMZac5YhloOQl2z9Zelh0onytmwbIsAAjAhAALYMnFWl-MxbGE86Ys6BA"

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 1. START ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🌸 **Welcome to Shreya AI** 🌸\n\n"
        "📢 **Main Menu:** Check voice from my channel.\n"
        "Bot ko use karne ke liye niche button dabayein."
    )
    kb = [[InlineKeyboardButton("Get Started 🚀", callback_data='ask_demo')]]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

# --- 2. BUTTONS LOGIC ---
async def handle_clicks(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Step: Get Started -> Ask for Demo
    if query.data == 'ask_demo':
        text = "Kya aap hamara voice demo check karna chahte hain?"
        kb = [[InlineKeyboardButton("Haan, Demo suniye 🎧", callback_data='play_voice')]]
        await query.message.edit_text(text, reply_markup=InlineKeyboardMarkup(kb))

    # Step: Play Voice + Show Plans + Ask for QR
    elif query.data == 'play_voice':
        try:
            await context.bot.send_audio(chat_id=query.message.chat_id, audio=VOICE_ID)
        except:
            pass
        
        text = (
            "💎 **Shreya AI Premium Plans:**\n\n"
            "🔥 **LIMITED STOCK!** 🔥\n\n"
            "1️⃣ 1 Day Access - ₹20\n"
            "2️⃣ 1 Week Access - ₹130\n\n"
            "Kya aap ye plans lena chahenge? Kya main aapko payment ke liye QR bhejun?"
        )
        kb = [[InlineKeyboardButton("Yes, QR bhejiye ✅", callback_data='final_qr')]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb))

    # Step: Final QR Code
    elif query.data == 'final_qr':
        caption = (
            "⚠️ **QR Valid for 5 Minutes Only**\n\n"
            "1. Scan karke ₹20 ya ₹130 ka payment karein.\n"
            "2. **Payment ke baad Screenshot zaroori bhejein.**\n\n"
            "Screenshot milte hi Shreya AI active ho jayega. ❤️"
        )
        try:
            await context.bot.send_photo(chat_id=query.message.chat_id, photo=open('qr.jpg', 'rb'), caption=caption)
        except:
            await query.message.reply_text("❌ QR file (qr.jpg) nahi mili! Kripya check karein.")

# --- 3. PHOTO HANDLER ---
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.photo:
        await update.message.reply_text("✅ Aapka screenshot mil gaya hai! Shreya AI aapki details verify kar rahi hai... ❤️")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_clicks))
    app.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    
    print("🚀 Shreya AI LIVE! Flow ekdum perfect hai.")
    app.run_polling()

if __name__ == '__main__':
    main()
