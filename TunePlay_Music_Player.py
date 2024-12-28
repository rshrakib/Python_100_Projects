from tkinter import Listbox

import pygame
import tkinter as tk

from tkinter.filedialog import askdirectory
import os

music_player = tk.Tk()
music_player.title("My Music Player")
music_player.geometry("450x355")
directory = askdirectory()
os.chdir(directory)
song_list = os.listdir()

play_list = tk.Listbox(music_player, font="Helvetica 12 bold", bg="yellow", selectmode=tk.SINGLE)

for item in song_list:
    pos = 0
    play_list.insert(pos,item)
    pos+=1

pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tk.ACTIVE))
    var.set(play_list.get(tk.ACTIVE))
    pygame.mixer.music.play()

def stop():
    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpuse():
    pygame.mixer.music.unpause()

button1 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text='play', command= play, bg = "blue", fg = "white")
button2 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text='stop', command= stop, bg = "red", fg = "white")
button3 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text='pause', command= pause, bg = "orange", fg = "white")
button4 = tk.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text='unpause', command= unpuse, bg = "black", fg = "white")

var = tk.StringVar()
song_title = tk.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
button1.pack(fill = 'x')
button2.pack(fill = 'x')
button3.pack(fill = 'x')
button4.pack(fill = 'x')
play_list.pack(fill = "both", expand = True)

music_player.mainloop()