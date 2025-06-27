import telegram
import os

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")  # Vagy ideiglenesen írd be direktbe a saját user ID-dat (pl.: 123456789)

bot = telegram.Bot(token=TOKEN)

try:
    bot.send_message(chat_id=CHAT_ID, text="✅ Sikeres kapcsolat: A bot működik!")
    print("✅ Üzenet elküldve sikeresen.")
except Exception as e:
    print(f"❌ Hiba történt: {e}")
