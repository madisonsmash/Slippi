# Madison Slippi
Webpage to host slippi files recorded at Madison smash events, made to replicate Slippi.gg (sorry for ripping you guys off)

## Requirements - Python 3.6
Nothing is required to host the page. However to add replays, you need to be able to run the python script which requires py-slippi, which can be installed with:

```
pip install py-slippi
```

After installing python and installing py-slippi, you can add replays using the following code. For this to function, you must have your replays put inside of folders inside replays, where the folder name will be used as the tournament name.

```
cd ${install-location}/include/py-scripts/
python replayparser.py
```

I haven't added code to move items out of their folders and delete the folders after the script is run, so you have to do that manually for now. If you do not, the replays will still be visible on the site, but won't be downloadable.

If you're using a beta build of Slippi, there are a few event codes, as well as character codes that py-slippi won't recognize (up until recently, it would simply exit with an exception, now it usually prints an error and keeps running, which is the desired behavior - though there are some exceptions that will still be thrown). If you should encounter an issue with an unknown character/event code while running the script, you can usually resolve them by adding the unknown codes to their respective dictionaries in your slippi-py install (Any given code should be missing in some dictionary in either id.py, event.py, or charset.py). If you don't get an unknown code on a given exception, the replay most recently displayed in your shell is likely corrupt/has some weird data on it caused by a different build of melee (20XX/UnclePunch), and the issue can be resolved by deleting that replay.