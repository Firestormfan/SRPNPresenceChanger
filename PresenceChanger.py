import pypresence
from pypresence import Presence
import time
import json

json_file = open('config.json','r',encoding='utf-8')
json_data = json.load(json_file)

client_id = json_data["client_id"]
state = json_data["state"]
details = json_data["details"]
start = json_data["start"]
large = json_data["large_image"]
largetxt = json_data["large_text"]
button = json_data["button"]
buttonurl = json_data["buttonURL"]

RPC = Presence(client_id)

if start == "False":
    while True:
        RPC.connect()
        RPC.update(state=(state),details=(details),large_image=(large),large_text=(largetxt),buttons=[{"label": button, "url": buttonurl}])
        print("接続しました")
elif start == "True":
    while True:
        RPC.connect()
        RPC.update(start=(time.time()),state=(state),details=(details),large_image=(large),large_text=(largetxt),buttons=[{"label": button, "url": buttonurl}])
        print("接続しました")