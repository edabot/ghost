import os
import sys
from subprocess import Popen
import schedule
from tkinter import *
from gpiozero import Servo, LED, Button
from time import sleep

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
    
def handleButton():
    if ghostActive == False:
        ghost()
        
demoButton.when_pressed=handleButton

schedule.every().day.at("01:00").do(showGhost)
    
def draw():
    schedule.run_pending()
    w.tk.after(1000, draw)