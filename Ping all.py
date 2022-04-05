from telethon import TelegramClient, events, sync
from config import *

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(pattern='/all'))
async def call_all(event):
    """Send a message when the command /start is issued."""
    chat = event.chat
    # get all the users and print them
    users = await bot.get_participants(chat)

    message = ''
    num = 0
    for i in users:

        if i.username != None:
            message += '@' + i.username + " "

        if num == 5:
            await event.respond(message)
            message = ''
            num = 0

        num += 1

    if message != "":
        await event.respond(message)
        message = ''
        num = 0


with bot:
    bot.run_until_disconnected()
