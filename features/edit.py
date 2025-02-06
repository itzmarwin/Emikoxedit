from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("my_bot", API_ID, API_HASH, BOT_TOKEN)

async def on_message_edit(client, message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Error: {e}")

app.add_handler(MessageHandler(on_message_edit, filters.edited_message))
app.run()
