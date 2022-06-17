import random, sys, json, websocket, requests

token = "YOUR_TOKEN"

guild = ''
channel = ''

ws = websocket.WebSocket()
ws.connect("wss://gateway.discord.gg/?v=9&encoding=json")
heartbeat_interval = json.loads(ws.recv())['d']['heartbeat_interval']

ws.send(
    json.dumps(
        {
            "op":2,
            "d":{
                "token":token, 
                "properties": {
                    "$os":"windows",
                    "$browser":"Discord",
                    "$device": "desktop" 
                    }
                }
            }
        )
    )

ws.send(
    json.dumps(
        {
            "op": 14,
            "d": 
                {
                    "guild_id": guild,
                    "typing": True,
                    "threads": False,
                    "activities": True,
                    "members": [],
                    "channels": {channel: [[0, 99]]}
                }
            }
        )
    )

#with open('data.json', 'a') as f:
print(json.loads(ws.recv()))

guilds = ws.recv()['d']['guilds']

for guild in guilds:
    if guild["id"] == '956638414424387615':
        for member in guild["members"]:
            print(member["user"]["id"])
            #json.dump(guild, f, indent=4)

ws.send(
    json.dumps(
        {
            "op": 14,
            "d": {
                    "guild_id": guild,
                    "channels": {channel: [[0, 99], [100, 199]]}
                }
            }
        )
    )
print(json.loads(ws.recv()))
