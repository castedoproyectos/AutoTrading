from telethon import TelegramClient, events, sync

client = TelegramClient('session_name',
                    "9u5zp9",
                    api_hash,
                    update_workers=1,
                    spawn_read_thread=False)
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
# messages stored in `posts.messages`
