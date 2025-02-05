from pyrogram import Client, filters
import random

# Cute waifu-style messages
cute_messages = [
    "❌ Oops! Your message got deleted because you edited it! 😅",
    "💔 Ah, no editing allowed! Your message was too cute to keep unchanged! 😇",
    "😳 You tried to edit! Your message was removed, waifu-style! ✨",
    "🎀 Your edit was noticed, but it’s gone now! Cute bot style! 🥰"
]

# This function will handle deleting edited messages in groups and send a cute message
async def delete_edited_message(client, message):
    try:
        # Delete the edited message
        await message.delete()

        # Send a cute reply in the same group
        reply = random.choice(cute_messages)  # Pick a random cute message
        await message.reply(reply, quote=True)  # Send the cute message
    except Exception as e:
        print(f"❌ Error deleting message: {e}")
