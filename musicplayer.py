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
paused = False #Song is not paused for now

def select():
    # bandcamp - visit for different formats
    songname = filedialog.askopenfile(initialdir="/", title="Select Song",
                                      filetypes=(("Song", ".mp3"), ("All Files", "*.*")))
    print(songname.name)
    songs_location.clear()
    songs_location.append(songname.name)

def errormessage(location):
    for location in songs_location:
        song_name = location.split("/")[-1]
        if (not song_name.endswith('.mp3')):
            return 1
        return 0

def playmusic():
    global now_playing_label
    for location in songs_location:
        if (errormessage(location)):
            error_message = "Not a .mp3 file. Error"
            new_error = tk.Label(background, text = error_message, bg = "red")
            new_error.place(relx = 0.4, rely = 0.4)
            return
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

def unpausemusic():
    mixer.music.unpause()

def play_pause():
    """
    Initially the song is playing so "paused" is False. So on pressing the button, the music pauses,
    and "paused" changes to True due to the toggling of "paused", so the second time you press
    the button, it will unpause it.
    """
    global paused
    if paused == True:
        unpausemusic()
    else:
        pausemusic()
    paused = not paused

def stopmusic():
    mixer.music.stop()


#canvas = tk.Canvas(frame, height=500, width=500, bg="black")
#canvas.pack()


background = tk.Frame(frame, bg="yellow")
background.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

select_song = tk.Button(frame, text="Select a Song", padx=15,
                        pady=5, fg="blue", bg="white", command=select)

# select_song.place(relwidth=0.2, relheight=0.05, relx=0.4, rely=0.9)
# select_song.pack(side = tk.LEFT)
select_song.place(relx = 0.0, rely = 0.0)

play = tk.Button(frame, text="Play", padx=15,
                 pady=5, fg="blue", bg="white", command=playmusic)

play.place(relx = 0.22, rely = 0.0)

pause = tk.Button(frame, text="Pause/Unpause", padx=15,
                  pady=5, fg="blue", bg="white", command=play_pause)

pause.place(relx = 0.345, rely = 0.0)

stop = tk.Button(frame, text="Stop", padx=15,
                 pady=5, fg="blue", bg="white", command=stopmusic)

stop.place(relx = 0.59, rely = 0.0)

frame.mainloop()
