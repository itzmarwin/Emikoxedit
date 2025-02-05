import asyncio
import threading
from flask import Flask
from pyrogram import Client, filters
from pyrogram.types import Message
from motor.motor_asyncio import AsyncIOMotorClient
import config  # Import config file
from pyrogram.errors import RPCError, FloodWait

# Initialize Bot
app = Client("EmikoXEdit", api_id=config.API_ID, api_hash=config.API_HASH, bot_token=config.BOT_TOKEN)

# Connect to MongoDB
mongo_client = AsyncIOMotorClient(config.MONGO_URL)
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
            await message.delete()  # Delete the edited message
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
    server.run(host="0.0.0.0", port=8080, use_reloader=False)  # Disable reloader to avoid issues

async def start_bot():
    print("✅ Bot is starting...")
    try:
        await app.start()
    except RPCError as e:
        if isinstance(e, FloodWait):
            print(f"⚠️ Flood wait error. Try again after {e.seconds} seconds.")  # Correct attribute here
        else:
            print(f"❌ RPC Error: {e}")

if __name__ == "__main__":
    # Run Flask in a separate thread
    threading.Thread(target=run_flask, daemon=True).start()

    # Run the bot using asyncio
    asyncio.run(start_bot())
    
