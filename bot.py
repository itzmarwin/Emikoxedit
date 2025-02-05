from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
import os
from flask import Flask
import threading

# Import config variables
from features.config import API_ID, API_HASH, BOT_TOKEN

# Initialize the bot
app = Client("nezuko_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Edit message delete function
async def on_message_edit(client, update):
    try:
        # Check if the update contains a message and the message is edited
        if update.edited_message:
            await update.edited_message.delete()  # Delete the edited message
    except Exception as e:
        print(f"Error deleting edited message: {e}")

# Add the handler to monitor edited messages in groups
app.add_handler(MessageHandler(on_message_edit, filters.update))  # Use filters.update

# Flask Server for Render Free Hosting
server = Flask(__name__)

@server.route('/')
def home():
    return "Bot is running!"

def run_flask():
    PORT = int(os.environ.get("PORT", 8080))  # Default port 8080
    server.run(host="0.0.0.0", port=PORT)

if __name__ == "__main__":
    print("✅ Bot is starting...")

    # Flask ko alag thread pe run karna
    threading.Thread(target=run_flask, daemon=True).start()

    # Pyrogram bot start karna
    app.run()
    
