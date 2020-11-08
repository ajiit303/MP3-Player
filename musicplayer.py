import pygame as pg
from pygame import mixer
import tkinter as tk
from tkinter import filedialog, Text
import os

frame = tk.Tk()
frame.title("MP3 Player")
songs_location = []

def select():
    for heading in background.winfo_children():
        if (not select_song):
            heading.destroy()
    # bandcamp - visit for different formats
    songname = filedialog.askopenfile(initialdir = "/", title = "Select Song",
    filetypes = (("Song", ".mp3"),("All Files","*.*")))
    print(songname.name)
    songs_location.append(songname.name)
    """
    for location in songs:
        label = tk.Label(background, text = location, bg = "red")
        label.pack()
    """
def playmusic():
    for location in songs_location:
        mixer.init()
        mixer.music.load(location)
        mixer.music.play()

canvas = tk.Canvas(frame, height = 700, width = 700, bg = "black")
canvas.pack()

#frame2 = tk.Tk()

background = tk.Frame(frame,bg = "yellow")
background.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

select_song = tk.Button(background, text = "Select a Song", padx = 10,
pady = 5, fg = "blue", bg = "white", command = select)

select_song.place(relwidth = 0.2, relheight = 0.05, relx = 0.4, rely = 0.9)

play = tk.Button(background, text = "Play", padx = 10,
pady = 5, fg = "blue", bg = "white", command = playmusic)

play.pack()

frame.mainloop()