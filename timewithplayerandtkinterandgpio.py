import os
import sys
from subprocess import Popen
import schedule
from tkinter import *
from gpiozero import Servo, LED
from time import sleep

movie = ("small.mp4")
servo = Servo(17)
led = LED(27)

def play_movie():
    os.system('killall omxplayer.bin')
    osmx = Popen(['omxplayer', '-b', movie])

def ghost():
    servo.min()
    led.on()
    sleep(1)
    led.off()
    sleep(3)
    servo.max()
    sleep(2)
    servo.detach()
    play_movie()
    sleep(6)
    led.on()
    sleep(1)
    led.off()

schedule.every().minute.do(ghost)
    

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
    ghost()
    ghost()
    w.tk.mainloop()