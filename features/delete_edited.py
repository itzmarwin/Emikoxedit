from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.group & filters.edited)
async def delete_edited_message(client: Client, message: Message):
    try:
        await message.delete()
    except Exception as e:
        print(f"Error deleting edited message: {e}")
      
