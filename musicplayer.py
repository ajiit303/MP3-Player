import pygame as pg
from pygame import mixer
import tkinter as tk
from tkinter import filedialog, Text
import os
import re

frame = tk.Tk()
frame.title("MP3 Player")
frame.configure(background = "black")
frame.geometry("500x500")
songs_location = []
now_playing_label = None

def select():
    # bandcamp - visit for different formats
    songname = filedialog.askopenfile(initialdir="/", title="Select Song",
                                      filetypes=(("Song", ".mp3"), ("All Files", "*.*")))
    print(songname.name)
    songs_location.clear()
    songs_location.append(songname.name)


def playmusic():
    global now_playing_label
    for location in songs_location:
        #song_name = location.split("/")[-1]
        pattern = r"(\\|\/)(.+(\\|\/))*(.+)\.(.+)$"
        song_name = re.search(pattern, location).group(4)
        
        if now_playing_label is None:
            now_playing_label = tk.Label(background, text = song_name, bg="red")
            now_playing_label.place(relx=0.0, rely=0.3)
        else:
            now_playing_label.configure(text = song_name)

        mixer.init()
        mixer.music.load(location)
        mixer.music.play()


def pausemusic():
    mixer.music.pause()


def stopmusic():
    mixer.music.stop()


#canvas = tk.Canvas(frame, height=500, width=500, bg="black")
#canvas.pack()


background = tk.Frame(frame, bg="yellow")
background.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

select_song = tk.Button(frame, text="Select a Song", padx=10,
                        pady=5, fg="blue", bg="white", command=select)

# select_song.place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.9)
select_song.pack(side = tk.TOP)

play = tk.Button(frame, text="Play", padx=10,
                 pady=5, fg="blue", bg="white", command=playmusic)

play.pack(side = tk.TOP)

pause = tk.Button(frame, text="Pause", padx=10,
                  pady=5, fg="blue", bg="white", command=pausemusic)

pause.pack(side = tk.TOP)

stop = tk.Button(frame, text="Stop", padx=10,
                 pady=5, fg="blue", bg="white", command=stopmusic)

stop.pack(side = tk.TOP)

frame.mainloop()
