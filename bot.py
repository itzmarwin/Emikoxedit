import os  # Yeh import likhna zaroori hai
import threading
from flask import Flask
from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN  
from features.edit import register_edit_handlers  

# Initialize Bot
app = Client("EmikoXEdit", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Register edit message handler
register_edit_handlers(app)

# Flask app (for Render keep-alive)
server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!"

def run_flask():
    PORT = int(os.getenv("PORT", 8080))  # Ensure os is imported
    server.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    print("✅ Bot is starting...")
    threading.Thread(target=run_flask, daemon=True).start()
    app.run()
