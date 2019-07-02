from telethon import TelegramClient, sync
from telethon.tl.functions.messages import GetHistoryRequest

class HandlerTelegram(object):
    
    def __init__(self, api_id, api_hash, phone, session_name):
        self.__api_id = None
        self.__api_hash = None
        self.__phone_number = None

        self.client = None
        self.channel = None

        self._set_api(api_id, api_hash)
        self._set_phone(phone)
        self.connect(session_name)

    def _set_api(self, api_id, api_hash):
        self.__api_id = api_id
        self.__api_hash = api_hash

    def _set_phone(self, phone):
        self.__phone_number = phone


    def connect(self, session_name):
        
        self.client = TelegramClient(session_name,
                                    self.__api_id,
                                    self.__api_hash)
        
        assert self.client.connect()
        if not self.client.is_user_authorized():
            self.client.send_code_request(self.__phone_number)
            me = self.client.sign_in(self.__phone_number, input('Enter code: '))

    
    def get_msn(self, name_channel):
        channel_entity = self.client.get_entity(name_channel)
        posts = self.client(GetHistoryRequest(
            peer=channel_entity,
            limit=100,
            offset_date=None,
            offset_id=0,
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))


hTelegram = HandlerTelegram("526632",
                            "eeb7b94dc683848287857f8bfa03aa58", 
                            "34657648827",
                            "test")


hTelegram.get_msn("Chollometro")