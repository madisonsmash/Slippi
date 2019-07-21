import json, re
from os import listdir
from os.path import isfile, join
from slippi import Game

replays = [f for f in listdir("replays") if isfile(join("replays", f))]

