from telethon import TelegramClient, events, sync

import requests
from bs4 import BeautifulSoup
import random

import json

# Use your own values from my.telegram.org
api_id = 1411433
api_hash = '1c42c133b5e0a9e9978797ab86ce0858'
bot_token = '1199435543:AAGbAM-KhMhxHSYw08uhQPXVOIQqe33-Dvo'

bot = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


@bot.on(events.NewMessage(pattern='/all'))
async def start(event):
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


@bot.on(events.NewMessage(pattern='/мем'))
async def mem(event):
    message = event.message.message
    ls = message.split(' ')
    print(ls)
    ls.pop(0)
    arg = " ".join(ls)

    url = 'https://www.google.co.in/search?q=мем про {}&source=lnms&tbm=isch'.format(arg) 

    #useragent = open('useragents.txt').read().split("\n")
    #user_agent = {"User-Agent": random.choice(useragent)}

    #proxy = open('proxy.txt').read().split("\n")

    #proxies = {
     #   'http': random.choice(proxy),

    #}

    r = requests.get(url,)
    text = r.text
    soup = BeautifulSoup(text, 'lxml')
    head = soup.find_all("img",)
    print(head)
    res = []
    b = 0
    for i in head:
        res.append(i.get("src"))

    res.pop(0)
    print(res)
    res_1 = random.choice(res)
    chat = event.chat
    await event.respond(res_1)

'''
def get_proxy():
    url = 'http://pubproxy.com/api/proxy?type=https'
    response = requests.get(url)

    # если адрес забанили или превышен лимит на запросы
    try:
        json_proxy = json.loads(response.text)
    except json.decoder.JSONDecodeError:
        last_proxy = {'ip_port': read_proxy()}
        return last_proxy

    # если не забанили, то создаём словарь с данными о прокси
    proxy_data = dict.fromkeys(['ip_port', 'ip', 'port', 'country', 'last_check'])

    proxy_data['ip_port'] = json_proxy['data'][0]['ipPort']
    proxy_data['ip'] = json_proxy['data'][0]['ip']
    proxy_data['port'] = json_proxy['data'][0]['port']
    proxy_data['country'] = json_proxy['data'][0]['country']
    proxy_data['last_check'] = json_proxy['data'][0]['last_checked']

    return proxy_data

'''
with bot:
    bot.run_until_disconnected()
