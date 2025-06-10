from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os

# Initialize window
root = Tk()
root.title("Music Player")
root.geometry("500x300")
root.configure(bg="#0f1a2b")
root.resizable(False, False)

# Initialize mixer
mixer.init()

# Load and play music
def load_and_play():
    filepath = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
    if filepath:
        mixer.music.load(filepath)
        mixer.music.play()
        song_label.config(text=os.path.basename(filepath))

# Stop music
def stop_music():
    mixer.music.stop()

# Widgets
song_label = Label(root, text="No song loaded", fg="white", bg="#0f1a2b", font=("Arial", 14))
song_label.pack(pady=20)

play_btn = Button(root, text="Load & Play", command=load_and_play)
play_btn.pack(pady=10)

stop_btn = Button(root, text="Stop", command=stop_music)
stop_btn.pack(pady=5)

root.mainloop()