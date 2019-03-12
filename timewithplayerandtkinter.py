import os
import sys
from subprocess import Popen
import schedule
import time
from datetime import datetime
from tkinter import *

movie = ("small.mp4")

def play_movie():
    os.system('killall osmxplayer.bin')
    osmx = Popen(['omxplayer', '-b', movie])

def job():
    play_movie()

schedule.every().minute.do(job)
    

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
    job()
    w.tk.mainloop()