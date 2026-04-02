import os
from flask import Flask
from threading import Thread
from telegram.ext import Updater, CommandHandler

# Render (Cloud) ke liye ye zaroori hai
app = Flask('')

@app.route('/')
def home():
    return "Mishu Store Bot is Live!"

def run():
    # Render hamesha port 8080 ya kisi environment port par chalta hai
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

# Jab koi Telegram par /start likhega
def start(update, context):
    update.message.reply_text("Namaste Teju! Aapka Mishu Store Bot ab Render par 24 ghante Live hai. 🚀")

def main():
    # Aapka asli Token maine yahan daal diya hai
    TOKEN = "7626359902:AAHw59y017zVfJ0O_G_1f6D7uN7Y26uT3W4" 
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    
    # Commands yahan add hoti hain
    dp.add_handler(CommandHandler("start", start))
    
    # Server ko background mein shuru karein
    Thread(target=run).start()
    
    # Bot ko shuru karein
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
