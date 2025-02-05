from pyrogram import Client, filters
import os
from motor.motor_asyncio import AsyncIOMotorClient

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

# Run Bot
if __name__ == "__main__":
    print("✅ Bot is starting...")
    app.run()
