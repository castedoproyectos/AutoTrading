from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest

import time

class TelegramHandler(object):

    def __init__(self):

        self._list_msn = list()

        self._sesion_name = "test"
        self._hash_id = "526632"
        self._hash_num = "eeb7b94dc683848287857f8bfa03aa58"

        self._client = TelegramClient(self._sesion_name,
                                self._hash_id,
                                self._hash_num)

        self._client.start()

        self._channel_entity = self._client.get_entity('https://t.me/joinchat/LbVznBRH92k0YavhYueMFg')


    def new_msn(self, list_msn):

        new = False
        for new_msn in list_msn:
            if new_msn not in self._list_msn and not new:
                new = True
            else:

            if nuevo:
                break
        
        return list_msn


    def get_msn(self):

        messages = list()

        posts = self._client(GetHistoryRequest(
            peer=self._channel_entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
    
        for it in enumerate(posts.messages):
            messages.append(posts.messages[it].message)

        