from telethon.tl.functions.messages import GetHistoryRequest
from telethon import TelegramClient, sync

client = TelegramClient('session_name',
                    '526632',
                    'eeb7b94dc683848287857f8bfa03aa58')

phone_number = '+34657648827'

assert client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone_number)
    me = client.sign_in(phone_number, input('Enter code: '))

channel_username='tehrandb' # your channel
channel_entity=client.get_entity(channel_username)
posts = client(GetHistoryRequest(
    peer=channel_entity,
    limit=100,
    offset_date=None,
    offset_id=0,
    max_id=0,
    min_id=0,
    add_offset=0,
    hash=0))