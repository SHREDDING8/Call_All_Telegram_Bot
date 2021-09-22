from telethon import TelegramClient, events, sync


# Use your own values from my.telegram.org
bot_token = '1199435543:AAGbAM-KhMhxHSYw08uhQPXVOIQqe33-Dvo'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


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


@bot.on(events.NewMessage(pattern='/all'))
async def update_base(event):
    pass

with bot:
    bot.run_until_disconnected()
