from pyrogram import Client, filters

# This function will handle deleting edited messages in groups
async def delete_edited_message(client, message):
    try:
        await message.delete()  # Delete the edited message
    except Exception as e:
        print(f"❌ Error deleting message: {e}")
