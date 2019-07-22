import json, re
from os import listdir
from os.path import isfile, join
from datetime import datetime
from slippi import Game

#codes for non-japanese tag characters
tagtranslator = {
    "\uff21": 'A',
    "\uff22": 'B',
    "\uff23": 'C',
    "\uff24": 'D',
    "\uff25": 'E',
    "\uff26": 'F',
    "\uff27": 'G',
    "\uff28": 'H',
    "\uff29": 'I',
    "\uff2a": 'J',
    "\uff2b": 'K',
    "\uff2c": 'L',
    "\uff2d": 'M',
    "\uff2e": 'N',
    "\uff2f": 'O',
    "\uff30": 'P',
    "\uff31": 'Q',
    "\uff32": 'R',
    "\uff33": 'S',
    "\uff34": 'T',
    "\uff35": 'U',
    "\uff36": 'V',
    "\uff37": 'W',
    "\uff38": 'X',
    "\uff39": 'Y',
    "\uff3a": 'Z',
    "\u3000": ' ',
    "\uff10": '0',
    "\uff11": '1',
    "\uff12": '2',
    "\uff13": '3',
    "\uff14": '4',
    "\uff15": '5',
    "\uff16": '6',
    "\uff17": '7',
    "\uff18": '8',
    "\uff19": '9',
    "\u2212": '-',
    "\uff0b": '+',
    "\uff1d": '=',
    "\uff01": '!',
    "\uff1f": '?',
    "\uff20": '@',
    "\uff05": '%',
    "\uff06": '&',
    "\uff04": '$',
    "\uff0e": '.',
}

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
        #generate list of players in game
        players = []
        for player in game.start.players:
            if player is not None:
                port = {}
                port['character'] = player.character
                port['costume'] = player.costume
                port['tag'] = player.tag
                if len(port['tag']) is not 0:
                    for key, replacement in tagtranslator.items():
                        port['tag'] = port['tag'].replace(key, replacement)
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