from flask import Flask, request
import telegram
import os

app = Flask(__name__)

# Környezeti változók
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
bot = telegram.Bot(token=TOKEN)

@app.route("/", methods=["GET"])
def index():
    return "✅ A bot fut Renderen! (GET)"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        data = request.json
        print(f"Received webhook: {data}")

        # TradingView-ból érkező adatok
        direction = data.get("direction", "")
        pair = data.get("pair", "Unknown")
        trigger_price = float(data.get("trigger_price", 0))
        time = data.get("time", "")
        trigger_type = data.get("trigger", "Unknown")
        
        # Pip kiszámítás (egyelőre 0.0001, devizánál EURUSD-re optimalizálva)
        pip = 0.00010

        # SL és TP számítása
        if direction.upper() == "LONG":
            sl = trigger_price - 10 * pip
            tp1 = trigger_price + 20 * pip
            tp2 = trigger_price + 30 * pip
        elif direction.upper() == "SHORT":
            sl = trigger_price + 10 * pip
            tp1 = trigger_price - 20 * pip
            tp2 = trigger_price - 30 * pip
        else:
            sl, tp1, tp2 = 0, 0, 0

        rr1 = round(abs(tp1 - trigger_price) / abs(trigger_price - sl), 2) if sl != trigger_price else 0
        rr2 = round(abs(tp2 - trigger_price) / abs(trigger_price - sl), 2) if sl != trigger_price else 0

        # Üzenet összeállítása
        message = (
            f"🚨 {direction.upper()} SIGNAL – {pair} (M5)\n"
            f"Entry: {trigger_price:.5f}\n"
            f"SL: {sl:.5f}\n"
            f"TP1: {tp1:.5f}\n"
            f"TP2: {tp2:.5f}\n"
            f"RR: {rr1}R / {rr2}R\n"
            f"Trigger: {trigger_type}\n"
            f"Time: {time}"
        )

        # Telegram üzenetküldés
        bot.send_message(chat_id=CHAT_ID, text=message, parse_mode=telegram.constants.ParseMode.MARKDOWN)

        return "✅ Üzenet elküldve Telegramra", 200

    except Exception as e:
        print(f"Error: {e}")
        return f"❌ Hiba: {e}", 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
