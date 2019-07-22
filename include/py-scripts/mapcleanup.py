import json, re
from os import listdir
from os.path import isfile, join

#get list of files
replays = [f for f in listdir("../../replays") if isfile(join("../../replays", f))]

#iterate to count removed files from map
removed = 0

#get existing data to prune from
with open('../../map.json', 'r') as file:
    map = json.load(file)

#remove mapped files that don't exist in replays
for index in list(map.keys()):
    if index not in replays:
        map.pop(index)
        removed = removed + 1

#dump contents
with open('../../map.json', 'w+') as f:
    json.dump(map, f, indent=4)

print("Removed "+str(removed)+" missing replays.")