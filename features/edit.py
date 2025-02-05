from pyrogram import Client, filters
from pyrogram.handlers import MessageHandler

# Edit message delete function
async def on_message_edit(client, message):
    try:
        if message.text:  # Check if the message is text
            await message.delete()  # Delete the edited message
    except Exception as e:
        print(f"Error deleting edited message: {e}")

# Add the handler to monitor edited messages in groups
app.add_handler(MessageHandler(on_message_edit, filters.group & filters.edited))
