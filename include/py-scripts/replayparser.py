import json, re
from os import listdir
from os.path import isfile, join
from datetime import datetime
from slippi import Game

#get list of files
replays = [f for f in listdir("../../replays") if isfile(join("../../replays", f))]

#get existing data (so we don't redo any existing replays)
with open('../../map.json', 'r') as file:
    map = json.load(file)

#iterate for counting new replays
newReplays = 0

#generate dictionary for each replay
for replaypath in replays:
    #if replay doesn't already exist
    if not replaypath in map:
        game = Game("../../replays//"+replaypath)
        data = {}
        players = []
        for player in game.start.players:
            if player is not None:
                port = {}
                port['character'] = player.character
                port['costume'] = player.costume
                port['tag'] = player.tag
                players.append(port)
            else:
                players.append(None)
        data['players'] = players
        data['stage'] = game.start.stage
        data['datetime'] = game.metadata.date.strftime("%m/%d/%Y, %H:%M:%S")
        data['searchdate'] = game.metadata.date.strftime("%Y-%m-%d")
        data['duration'] = game.metadata.duration
        map[replaypath] = data
        newReplays = newReplays + 1

#dump contents
with open('../../map.json', 'w+') as f:
    json.dump(map, f, indent=4)

print("Successfully mapped "+str(newReplays)+" new replays.")