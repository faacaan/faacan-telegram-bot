import os
import telegram
from telegram.error import TelegramError

# Környezeti változók
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

# Telegram bot inicializálása
bot = telegram.Bot(token=BOT_TOKEN)

# Üzenet küldése tesztként
try:
    bot.send_message(chat_id=CHAT_ID, text="🚀 Faacan bot aktív és működik!")
except TelegramError as e:
    print(f"Hiba az üzenetküldés során: {e}")
