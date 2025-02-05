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

# Edit Message Handler (To delete edited messages)
@app.on_message(filters.group & filters.text)
async def check_edit(client, message):
    if message.edit_date:  # Check if the message is edited
        try:
            await message.delete()
            await message.reply_text(
                "✨ **Oops! You edited your message, so I had to delete it!**\n\n"
                "🚀 **Next time, think before you send!**",
                reply_to_message_id=message.message_id
            )
        except Exception as e:
            print(f"❌ Error deleting edited message: {e}")

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

    # Pyrogram bot run karna
    app.run()
    
