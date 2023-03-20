import tkinter as tk
from tkinter import filedialog
import os
from pygame import mixer

def browse_directory():
    """Browse for the directory and update the directory label"""
    global directory_label
    global directory 
    directory = filedialog.askdirectory()
    if directory:
        directory_label.config(text=directory)
        check_directory(directory)

def check_directory(directory):
    """Get a list of audio files in the directory and display them in the listbox widget"""
    global file_listbox
    file_listbox.delete(0, tk.END)  # clear existing contents
    file_list = os.listdir(directory)
    for file_name in file_list:
        if os.path.isfile(os.path.join(directory, file_name)):
            ext = os.path.splitext(file_name)[1].lower()
            if ext in ['.mp3', '.wav', '.ogg']:
                file_listbox.insert(tk.END, file_name)

# Initialize Mixer
mixer.init()

# Create the main window
canvas = tk.Tk()
canvas.title("AsteriX")
canvas.geometry("1280x720")
canvas.config(bg = 'black')


# Set Image for buttons
prev_img = tk.PhotoImage(file= 'Icons\prev.png')
play_img = tk.PhotoImage(file= 'Icons\play-alt.png')
pause_img = tk.PhotoImage(file= 'Icons\pause.png')
next_img = tk.PhotoImage(file= 'Icons\pnext.png')

def play():
    """play music"""
    song = file_listbox.curselection()
    song_name = file_listbox.get(song)  
    song_label.config(text = song_name)
    mixer.music.load(directory + "\\" + song_name)
    mixer.music.play()

def pause():
    """pause music"""
    if pauseButton["text"] == "Pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton['text'] = "Pause"

def play_next():
    """play next song"""
    song = file_listbox.curselection()
    next_song = song[0] + 1
    next_song_name = file_listbox.get(next_song)
    song_label.config(text = next_song_name)
    mixer.music.load(directory + "\\" + next_song_name)
    mixer.music.play()
    file_listbox.select_clear(0, 'end')
    file_listbox.activate(next_song)
    file_listbox.select_set(next_song)

def play_prev():
    """play previous song"""
    song = file_listbox.curselection()
    next_song = song[0] - 1
    next_song_name = file_listbox.get(next_song)
    song_label.config(text = next_song_name)
    mixer.music.load(directory + "\\" + next_song_name)
    mixer.music.play()
    file_listbox.select_clear(0, 'end')
    file_listbox.activate(next_song)
    file_listbox.select_set(next_song)

# Create the file listbox widget
file_listbox = tk.Listbox(canvas, fg = "cyan", bg = "black", width = 100, font = ('poppins', 14))
file_listbox.pack(padx = 15, pady = 15)

# Create song label widget
song_label = tk.Label(canvas, text = '', bg = 'black', fg = 'yellow', font = ('poppins', 10))
song_label.pack(pady = 15)

# Create button container
top = tk.Frame(canvas, bg = 'black')
top.pack(padx = 10, pady = 5, anchor = 'center')

# Setup play, pause, playNext, playPrev buttons
prevButton = tk.Button(canvas, text = 'Prev', image = prev_img, bg='black', borderwidth= 0, command=play_prev)
prevButton.pack(pady = 15, in_ = top, side = 'left')

playButton = tk.Button(canvas, text = 'Play', image= play_img, bg='black', borderwidth= 0, command=play)
playButton.pack(pady = 15, in_ = top, side = 'left')

pauseButton = tk.Button(canvas, text = 'Pause', image= pause_img, bg='black', borderwidth=0, command=pause)
pauseButton.pack(pady = 15, in_ = top, side = 'left')

nextButton = tk.Button(canvas, text = 'Next', image= next_img, bg='black', borderwidth= 0, command=play_next)
nextButton.pack(pady = 15, in_ = top, side = 'left')

# Create browse button and directory label container
browse = tk.Frame(canvas, bg = 'black')
browse.pack(padx = 10, pady = 5, anchor = 'center')

# Create the browse button and directory label
directory_label = tk.Label(canvas, text="No directory selected.")
directory_label.pack(padx = 10, pady=10, in_ = browse, side = 'left')
browse_button = tk.Button(canvas, text="Browse", command=browse_directory)
browse_button.pack(pady=10, in_ = browse, side = 'left')

# Start Mainloop
canvas.mainloop()