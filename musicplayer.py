import pygame as pg
import tkinter as tk
from tkinter import filedialog, Text
import os

frame = tk.Tk()

canvas = tk.Canvas(frame, height = 700, width = 700, bg = "black")
canvas.pack()

background = tk.Frame(frame,bg = "yellow")
background.place(relwidth = 0.8, relheight = 0.8, relx = 0.1, rely = 0.1)

select_song = tk.Button(frame, text = "Select a Song", padx = 10,
pady = 5, fg = "blue", bg = "white")



select_song.pack()

frame.mainloop()