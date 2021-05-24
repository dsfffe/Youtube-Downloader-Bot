from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just send a yputube Link not playlist"
    await message.reply_text(helptxt)
