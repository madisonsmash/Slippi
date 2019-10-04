# Madison Slippi
Webpage to host slippi files recorded at Madison smash events, made to replicate Slippi.gg (sorry for ripping you guys off)

## Adding replays
To add replays, add a folder with the name of your tournament to the replays folder, move your replay files into that folder and run include/py-scripts/replayerparser.py to add your files' data to the json map of the replays directory
(To do this, install python, add it to your path, run 'pip install py-slippi' to download the python slippi libraries for parsing game data, cd to py-scripts and run 'python replayparser.py') (or just add the files to the replays directory, make a pull request and @ me on discord @BigAndrew#7491) To make the files, you have to move them out of that folder and just into replays - I'll probably write some code to move them all out of the directory eventually but I'm too lazy right now.

In case of removing replays, install python and run mapcleanup.py the same way you run replayparser.py.
