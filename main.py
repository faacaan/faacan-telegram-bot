import os
import telegram

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TOKEN)

try:
    bot.send_message(chat_id=CHAT_ID, text="✅ Faacan bot aktív és működik!")
    print("✅ Üzenet sikeresen elküldve.")
except Exception as e:
    print(f"❌ Hiba az üzenetküldés során: {e}")
