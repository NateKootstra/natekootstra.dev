import json
from datetime import datetime, timezone

from datamanager import getData

def getChannels():
    return getData("chat/channels.json")["list"]

def getChannel(channel):
    return getData(f"chat/channels/{channel}.json")

def getTimestamp():
    return int(datetime.now(timezone.utc).timestamp())

print(getTimestamp())