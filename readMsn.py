from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

import time

client = TelegramClient('session_name',
                    "526632",
                    "eeb7b94dc683848287857f8bfa03aa58")

client.start()

channel_entity=client.get_entity('https://t.me/joinchat/LbVznBRH92k0YavhYueMFg')
 
last_msn = ""
while True:

    posts = client(GetHistoryRequest(
        peer=channel_entity,
        limit=100,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

#    print("Evaluacion --")
#    print(last_msn)
#    print(posts.messages[0].message)

    if last_msn != posts.messages[0].message:
        last_msn = posts.messages[0].message
        print("Nuevo mensaje")
        print(last_msn)
    else:
        print("No hay nuevo mensaje")

    time.sleep(5)
    
a = 2