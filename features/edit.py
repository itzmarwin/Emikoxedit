from pyrogram import Client
from pyrogram.types import Message  # Correct import for Message

# This function will handle deleting edited messages in groups
async def delete_edited_message(client: Client, message: Message):
    try:
        # Delete the edited message
        await message.delete()
        logging.info(f"Deleted edited message from {message.from_user.username}")
    except Exception as e:
        logging.error(f"Error deleting message: {e}")
