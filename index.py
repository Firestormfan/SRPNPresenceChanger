import json
import time

from pypresence import Presence

with open('config.json', 'r', encoding='utf-8') as f:
    json_data = json.load(f)

RPC = Presence(str(json_data['client_id']))
RPC.connect()
print('Rich Presenceに接続しました！リッチなDiscordを楽しんで！')

RPC.update(
    start=time.time() if json_data['start'] else None,
    state=json_data['state'],
    details=json_data['details'],
    large_image=json_data['large_image'],
    large_text=json_data['large_text'],
    buttons=[
        {
            'label': json_data['button_name'],
            'url': json_data['button_url']
        }
    ] if json_data['button'] else None
)

try:
    while True:
        time.sleep(15)
except KeyboardInterrupt:
    RPC.close()
