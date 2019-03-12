import os
import sys
from subprocess import Popen

movie = ("small.mp4")
os.system('killall omxplayer.bin')
osmx = Popen(['omxplayer', '-b', movie])
player = True
    