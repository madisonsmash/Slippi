import json, re
from os import listdir
from os.path import isfile, join
from datetime import datetime

replays = [f for f in listdir("../../replays") if isfile(join("../../replays", f))]

#get existing data (so we don't redo any existing replays)
with open('../../map.json', 'r') as file:
    map = json.load(file)

#generate dictionary for each replay
for replaypath in replays:
    #if replay doesn't already exist
    if not replaypath in map['replays']:
        map['replays'].append(replaypath)

#dump contents
with open('../../map.json', 'w+') as f:
    json.dump(map, f, indent=4)