import os
import sys
from subprocess import Popen
import schedule
import time
from datetime import datetime

movie = ("small.mp4")

def job(t):
    os.system('killall osmxplayer.bin')
    osmx = Popen(['omxplayer', '-b', movie])
    player = True

schedule.every().minute.do(job, datetime.now())

while True:
    schedule.run_pending()
    
