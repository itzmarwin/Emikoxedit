from pyrogram import Client, filters
from pyrogram.types import Message

# Edited Message Handler
@Client.on_message(filters.group & filters.text)
async def delete_edited_messages(client: Client, message: Message):
    if message.edit_date:  # Check if the message is edited
        try:
            await message.delete()
            await message.reply_text(
                f"**Hey {message.from_user.mention}, your edited message has been deleted!** 🚀",
                reply_to_message_id=message.message_id
            )
        except Exception as e:
            print(f"❌ Error deleting edited message: {e}")
