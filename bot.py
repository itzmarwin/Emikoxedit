from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import os
from flask import Flask
import threading
import asyncio
from features.config import API_ID, API_HASH, BOT_TOKEN

app = Client("nezuko_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

async def on_message_edit(client, message):
    try:
        await message.delete()  # Edited message delete karega
    except Exception as e:
        print(f"Error: {e}")

# Edited messages ke liye handler
app.add_handler(MessageHandler(on_message_edit, filters.edited))  # Updated filter

server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!"

def run_flask():
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

async def start_bot():
    print("✅ Bot started!")
    await app.start()

if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    asyncio.run(start_bot())
