import pygame as pg
import tkinter as tk
from tkinter import filedialog, Text
import os
from tkinter import *
from tkinter import filedialog
from pygame import mixer
# This is Truong's Branch
frame = tk.Tk()

canvas = tk.Canvas(frame, height = 700, width = 700, bg = "black")
canvas.pack()

background = tk.Frame(frame,bg = "yellow")
background.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

#uigansdkukwhms,
#Initialize pygame mixer
#mixer.init()
#mixer.music.load()
#mixer.music.play()
class MusicPlayer:
    def __init__(self, window):
        pass


#instantiate class MusicPlayer
player = MusicPlayer(frame)



frame.mainloop()