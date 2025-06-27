from flask import Flask, request
import telegram
import os

app = Flask(__name__)

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
bot = telegram.Bot(token=TOKEN)

@app.route('/')
def home():
    return 'Faacan bot aktív!'

@app.route('/webhook', methods=['POST'])
def webhook():
    try:
        data = request.json
        message = f"""
📊 ÚJ TRADINGVIEW SZIGNÁL

💥 Pár: {data.get('pair')}
🎯 Irány: {data.get('direction')}
🎯 Entry: {data.get('entry')}
📍 SL: {data.get('sl')}
🎯 TP: {data.get('tp')}
"""
        bot.send_message(chat_id=CHAT_ID, text=message.strip())
        return 'OK', 200
    except Exception as e:
        print(f"❌ Hiba: {e}")
        return 'Hiba', 500

if __name__ == '__main__':
    app.run()
