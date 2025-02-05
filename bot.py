import asyncio
from flask import Flask
from threading import Thread
from pyrogram import Client, filters
from pyrogram.types import Message

# Bot Configuration
API_ID = 21346925  
API_HASH = "908c9a085a238d1cd484a4269c887234"  
BOT_TOKEN = "7733194032:AAGSzRGA3ihA_fvngTa0h60sBkBKX6BjWaQ"  

# Initialize Bot
app = Client("EmikoXEdit", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Flask Web Server (to keep bot alive on Render)
server = Flask(__name__)

@server.route('/')
def home():
    return "Emiko X Edit Bot is Running!"

def run_web():
    server.run(host="0.0.0.0", port=8080)

# Function to delete edited messages
@app.on_message(filters.group & filters.create(lambda _, __, m: bool(m.edit_date)))
async def delete_edited_message(client: Client, message: Message):
    try:
        await message.delete()
        await message.reply_text(
            f"**Hey {message.from_user.mention}, your edited message has been deleted.**"
        )
    except Exception as e:
        print(f"Error deleting message: {e}")

# Start Flask Server & Bot
if __name__ == "__main__":
    Thread(target=run_web).start()  # Flask server run karega
    print("Bot is starting...")
    app.run()
    
