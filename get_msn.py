import os
import sys
import time
from telethon import TelegramClient, events, utils

client = TelegramClient('name', api_id, api_hash)

channel = 'MyChannel'

@client.on(events.NewMessage(chats=channel))
async def my_event_handler(event):
    if 'Surname' in event.raw_text:
        messageId = event.message.id +1
        #wait print(client.iter_messages(channel,offset_id=messageId)
        for msg in client.iter_messages(channel,offset_id=messageId):
            print(msg)