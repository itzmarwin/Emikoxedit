import threading
from flask import Flask
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN  # Import config
import features.edit  # Import edit message feature

# Initialize Bot
app = Client("EmikoXEdit", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Flask app (for Render keep-alive)
server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!"

def run_flask():
    PORT = int(os.environ.get("PORT", 8080))  # Default port 8080
    server.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    print("✅ Bot is starting...")

    # Flask ko alag thread pe run karo
    threading.Thread(target=run_flask, daemon=True).start()

    # Bot start karo
    app.run()
