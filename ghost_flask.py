import os
import sys
from subprocess import Popen
import schedule
from tkinter import *
from gpiozero import Servo, LED, Button
from time import sleep
from flask import request, Flask, render_template
from random import randrange

movie_prefix = "/home/pi/Documents/ghost/movies/ghost_sideways_"
movie_suffix = ".mp4"
lensCover = Servo(17)
projectorButton = LED(27)
demoButton = Button(3)
ghostActive = False

def play_movie():
    os.system('killall omxplayer.bin')
    osmx = Popen(['omxplayer', '-b', movie_prefix+str(randrange(1,4))+movie_suffix])

def showGhost():
    ghostActive = True
    lensCover.min()
    projectorButton.on()
    sleep(1)
    projectorButton.off()
    sleep(3)
    play_movie()
    sleep(4)
    lensCover.max()
    sleep(2)
    lensCover.detach()
    sleep(6)
    projectorButton.on()
    sleep(1)
    projectorButton.off()
    ghostActive = False

app=Flask(__name__)

@app.route('/', methods=["GET"])
def api_root():
    return render_template('index.html')

@app.route('/playghost', methods=["GET"])
def playGhost():
    if not ghostActive:
        showGhost()
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()
