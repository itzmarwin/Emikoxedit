from pyrogram import Client, filters
from pyrogram.types import Message

def register_edit_handlers(app: Client):
    @app.on_message(filters.group & filters.text)
    async def check_edit(client: Client, message: Message):
        if message.edit_date:  # Check if the message is edited
            try:
                await message.delete()
                await message.reply_text(
                    f"✨ **Hey {message.from_user.mention}, edited messages are not allowed!**",
                    quote=True
                )
            except Exception as e:
                print(f"❌ Error deleting edited message: {e}")
