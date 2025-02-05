from pyrogram import Client, filters
import os
from motor.motor_asyncio import AsyncIOMotorClient
from flask import Flask
import threading
import logging
import random
import time

# Importing the delete function from the edit feature
from features.edit import delete_edited_message

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

# Setup logging
logging.basicConfig(level=logging.INFO)

# Cute messages to reply with
cute_messages = [
    "Aww, you edited your message! 😢 But don't worry, I'm here to fix it! 🛠️",
    "Oops! Looks like you changed something. Let me clean that up for you! 💖",
    "You edited your message! 😳 Don't worry, I'll take care of that! ✨",
    "Hey, I saw that! Editing, huh? Let me remove that for you! ✨"
]

# Start Command
@app.on_message(filters.command("start") & filters.private)
async def start(client, message):
    await message.reply("👋 Hello! I'm Emiko X Edit. Add me to a group as admin to use my features.")

# Edit Message Handler (To delete edited messages)
@app.on_message(filters.group)
async def on_message(client, message):
    # Check if the message is edited
    if message.edit_date:  # If the message is edited
        logging.info(f"Edited message detected: {message.text}")
        
        # Calling the delete_edited_message function
        await delete_edited_message(client, message)

        # Send a cute reply in the same group
        reply = random.choice(cute_messages)  # Pick a random cute message
        await message.reply(reply, quote=True)  # Send the cute message

# Flask app
server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!"

def run_flask():
    # PORT ko environment variable se get karo
    PORT = int(os.environ.get("PORT", 8080))  # Agar PORT na ho, toh 8080 default rahega
    server.run(host="0.0.0.0", port=PORT)

async def start_bot():
    while True:
        try:
            await app.start()
            break
        except Exception as e:
            logging.error(f"Error while starting bot: {e}")
            logging.info("Reconnecting in 10 seconds...")
            time.sleep(10)

if __name__ == "__main__":
    print("✅ Bot is starting...")

    # Flask ko alag thread pe run karo
    threading.Thread(target=run_flask, daemon=True).start()

    # Start Pyrogram bot
    asyncio.run(start_bot())  # Use asyncio to handle bot startup with error handling
