import tkinter as tk
from tkinter import *
import os
from tkmacosx import Button

# Disclaimer - Does not run optimally in fullscreen as of yet

# Make root variable

root = tk.Tk()

# Make a Window and its characterisiics!

root.title("Applications GUI")
canvas = tk.Canvas(root, height=600, width=760, bg="#3c3836", borderwidth=0, highlightthickness=0)
canvas.pack()

# Disables the maximuze button

root.resizable(False, False)

# Make a frame

frame = tk.Frame(root, bg="#3c3836")
frame.place(relheight=0.95, relwidth=0.92, relx=0.04, rely=0.04)

# Add any labels

Label(frame, text="Welcome!", font=14, bg="#3c3836", fg="#928374").grid(row=1, column=3, padx=5, pady=4)
Label(frame, text="by Kyle Cartier", bg="#3c3836", fg="#928374").grid(row=2, column=3, padx=3, pady=1)
Label(frame, text="-------------", bg="#3c3836", fg="#928374").grid(row=3, column=2, padx=3, pady=1)
Label(frame, text="-------------", bg="#3c3836", fg="#928374").grid(row=3, column=3, padx=3, pady=1)
Label(frame, text="-------------", bg="#3c3836", fg="#928374").grid(row=3, column=4, padx=3, pady=1)
Label(frame, text="Main Apps", bg="#3c3836", fg="#928374").grid(row=3, column=1, padx=3, pady=1)
Label(frame, text="Other Apps", bg="#3c3836", fg="#928374").grid(row=3, column=5, padx=3, pady=1)
Label(frame, text="Other Apps", bg="#3c3836", fg="#928374").grid(row=3, column=5, padx=3, pady=1)
Label(frame, text="->", bg="#3c3836", fg="#928374").grid(row=10, column=2, padx=3, pady=1)
Label(frame, text="<-", bg="#3c3836", fg="#928374").grid(row=10, column=4, padx=3, pady=1)
Label(frame, text="Click Exit to close the app", bg="#3c3836", fg="#928374").grid(row=11, column=3, padx=3, pady=1)

# Define functions for buttons

def open_file(): 
    os.system('open /System/Library/CoreServices/Finder.app')

def open_chrome():
    os.system('open /Applications/Google\ Chrome.app')

def open_settings():
    os.system('open /System/Applications/System\ Settings.app')

def open_store():
    os.system('open /System/Applications/App\ Store.app')

def open_vlc():
    os.system('open /Applications/VLC.app')

def open_excel():
    os.system('open /Applications/Microsoft\ Excel.app')

def open_calendar():
    os.system('open /System/Applications/Calendar.app')

def open_notepad():
    os.system('open /System/Applications/Notes.app')

def open_calculator():
    os.system('open /System/Applications/Calculator.app')

def open_taskmanager():
    os.system('open /System/Applications/Utilities/Activity\ Monitor.app')

def open_photos():
    os.system('open /System/Applications/Photos.app')

def open_cmd():
    os.system('open /System/Applications/Utilities/Terminal.app ')

def Exit():
    root.destroy()
 
# Buttons!
  
# Left Side

button_1 = Button(frame, text="Files", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_file)
button_1.grid(row=4, column=1, padx=10, pady=10)

button_2 = Button(frame, text="Chrome", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_chrome)
button_2.grid(row=5, column=1, padx=10, pady=10)

button_3 = Button(frame, text="System Settings", padx=8, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_settings)
button_3.grid(row=6, column=1, padx=10, pady=10)

button_4 = Button(frame, text="App Store", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_store)
button_4.grid(row=7, column=1, padx=10, pady=10)

button_5 = Button(frame, text="VLC", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_vlc)
button_5.grid(row=8, column=1, padx=10, pady=10)

button_6 = Button(frame, text="Microsoft Excel", padx=8, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_excel)
button_6.grid(row=9, column=1, padx=10, pady=10)

# Right Side

button_7 = Button(frame, text="Calendar", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_calendar)
button_7.grid(row=4, column=5, padx=10, pady=10)

button_8 = Button(frame, text="Notes", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_notepad)
button_8.grid(row=5, column=5, padx=10, pady=10)

button_9 = Button(frame, text="Calculator", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_calculator)
button_9.grid(row=6, column=5, padx=10, pady=10)

button_10 = Button(frame, text="Activity Monitor", padx=8, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_taskmanager)
button_10.grid(row=7, column=5, padx=10, pady=10)

button_11 = Button(frame, text="Photos", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_photos)
button_11.grid(row=8, column=5, padx=10, pady=10)

button_12 = Button(frame, text="Terminal", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=open_cmd)
button_12.grid(row=9, column=5, padx=10, pady=10)

# Exit Button (In the middle on the bottom)

exit_button = Button(frame, text="Exit", padx=25, pady=10, fg="#282828", bg="#928374", activebackground="#928374", activeforeground="#282828", borderless=1, focuscolor="", command=Exit)
exit_button.grid(row=10, column=3, padx=10, pady=10)

root.mainloop()

# End of code


