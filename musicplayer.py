import pygame as pg
import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
# This is Truong's Branch
frame = tk.Tk()



#uigansdkukwhms,
#Initialize pygame mixer
#mixer.init()
#mixer.music.load()
#mixer.music.play()
class MusicPlayer:
    def __init__(self, frame):
        frame.geometry('320x300')
        frame.title('mp3player')
        play = Button(frame, text='play', width=15)
        pause = Button(frame, text='pause', width=15)
        play.place(x=0,y=40)
        pause.place(x=110, y=40)



    def play(self):
        pass

#instantiate class MusicPlayer

player = MusicPlayer(frame)



frame.mainloop()