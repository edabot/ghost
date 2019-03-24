import os
import sys
from subprocess import Popen
import schedule
from tkinter import *
from gpiozero import Servo, LED, Button
from time import sleep

movie = ("ghost_sideways_2.mp4")
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

schedule.every().minute.do(showGhost)
schedule.every().day.at("01:00").do(showGhost)

class Fullscreen_Window:

    def __init__(self):
        self.tk = Tk()
        self.tk.attributes('-zoomed', True)  # This just maximizes it so we can see the window. It's nothing to do with fullscreen.
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk["bg"] = "black"
        self.tk["cursor"] = "none"
        self.toggle_fullscreen()

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
    
def draw():
    schedule.run_pending()
    w.tk.after(1000, draw)

if __name__ == '__main__':
    w = Fullscreen_Window()
    draw()
    w.tk.mainloop()