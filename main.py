from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Környezeti változók (Renderen beállítva)
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

bot = telegram.Bot(token=TOKEN)

@app.route("/", methods=["GET"])
def index():
    return "✅ A bot fut Renderen! (GET)"

@app.route("/", methods=["POST"])
def webhook():
    try:
        data = request.json
        message = f"📩 Új TradingView jelzés:\n\n{data}"
        bot.send_message(chat_id=CHAT_ID, text=message)
        return "✅ Üzenet elküldve Telegramra", 200
    except Exception as e:
        return f"❌ Hiba az üzenetküldés során: {e}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
