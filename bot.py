from pyrogram import Client, filters
import os
from motor.motor_asyncio import AsyncIOMotorClient
from flask import Flask
import threading

# Config Variables
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
MONGO_URL = os.getenv("MONGO_URL", "")

# Initialize Bot
app = Client("EmikoXEdit", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Connect to MongoDB
mongo_client = AsyncIOMotorClient(MONGO_URL)
db = mongo_client["EmikoXEdit"]
broadcast_collection = db["broadcast_users"]

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("👋 Hello! I'm Emiko X Edit. Add me to a group as admin to use my features.")

# Flask app
server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!"

def run_flask():
    # PORT ko environment variable se get karo
    PORT = int(os.environ.get("PORT", 8080))  # Agar PORT na ho, toh 8080 default rahega
    server.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    print("✅ Bot is starting...")

    # Flask ko alag thread pe run karo
    threading.Thread(target=run_flask, daemon=True).start()

    # Pyrogram bot run karna
    app.run()
