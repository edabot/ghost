import os
import sys
from subprocess import Popen
import schedule
from tkinter import *
from gpiozero import Servo, LED, Button
from time import sleep
from flask import request, Flask, render_template

movie = ("/home/pi/Documents/ghost/ghost_sideways_2.mp4")
lensCover = Servo(17)
projectorButton = LED(27)
demoButton = Button(3)
ghostActive = False

def play_movie():
    os.system('killall omxplayer.bin')
    osmx = Popen(['omxplayer', '-b', movie])

def showGhost():
    ghostActive = True
    lensCover.min()
    projectorButton.on()
    sleep(1)
    projectorButton.off()
    sleep(3)
    lensCover.max()
    sleep(2)
    lensCover.detach()
    play_movie()
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
    play_movie()
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run()
