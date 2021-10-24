from telethon import TelegramClient, events, sync
import re


import os

print("Введите ваш API_ID")
api_id = input()
print("Введите ваш API_HASH")
api_hash = input()
print("Вход выполнен!")

regex = r"BTC_CHANGE_BOT\?start="

client = TelegramClient('session', api_id, api_hash)



@client.on(events.NewMessage())
async def normal_handler(event):
    user_mess = event.message.to_dict()['message']
    m_from = event.message.to_dict()
    if re.search(r'BTC_CHANGE_BOT\?start=', user_mess):
        m = re.search(r'c_\S+', user_mess.replace(" ",""))
        print(m.group())
        await client.send_message('BTC_CHANGE_BOT', '/start ' + m.group(0))
    elif re.search(r'ETH_CHANGE_BOT\?start=', user_mess):
        m = re.search(r'c_\S+', user_mess.replace(" ",""))
        await client.send_message('ETH_CHANGE_BOT', '/start ' + m.group(0))
        print(m.group(0))
client.start()
client.run_until_disconnected()
