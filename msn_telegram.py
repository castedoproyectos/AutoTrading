from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest
import time

client = TelegramClient('session_name',
                    '526632',
                    'eeb7b94dc683848287857f8bfa03aa58')
client.start()

last_msg = ""
while True:
    # Se hace con el test
    channel_entity=client.get_entity('https://t.me/joinchat/LbVznBRH92k0YavhYueMFg')
    posts = client(GetHistoryRequest(
        peer=channel_entity,
        limit=1,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0))

    msg = posts.messages[0].message
    if msg is not last_msg:
        print(msg)
        last_msg = msg

    time.sleep(5)



