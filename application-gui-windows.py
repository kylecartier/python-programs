import tkinter as tk
from tkinter import *
import os

# Disclaimer - Does not run optimally in fullscreen as of yet

# Make root variable

root = tk.Tk()

# Make a Window and its characterisiics!

root.title("Applications GUI")
canvas = tk.Canvas(root, height=600, width=640, bg="#1d1d1d", borderwidth=0, highlightthickness=0)
canvas.pack()

# Disables the maximuze button

root.resizable(False, False)

# Make a frame

frame = tk.Frame(root, bg="#1d1d1d")
frame.place(relheight=0.95, relwidth=0.92, relx=0.04, rely=0.04)

# Add any labels

Label(frame, text="Welcome!", font=14, bg="#1d1d1d", fg="#555555").grid(row=1, column=3, padx=5, pady=4)
Label(frame, text="by Kyle Cartier", bg="#1d1d1d", fg="#555555").grid(row=2, column=3, padx=3, pady=1)
Label(frame, text="-------------", bg="#1d1d1d", fg="#555555").grid(row=3, column=2, padx=3, pady=1)
Label(frame, text="-------------", bg="#1d1d1d", fg="#555555").grid(row=3, column=3, padx=3, pady=1)
Label(frame, text="-------------", bg="#1d1d1d", fg="#555555").grid(row=3, column=4, padx=3, pady=1)
Label(frame, text="Main Apps", bg="#1d1d1d", fg="#555555").grid(row=3, column=1, padx=3, pady=1)
Label(frame, text="Other Apps", bg="#1d1d1d", fg="#555555").grid(row=3, column=5, padx=3, pady=1)
Label(frame, text="->", bg="#1d1d1d", fg="#555555").grid(row=10, column=2, padx=3, pady=1)
Label(frame, text="<-", bg="#1d1d1d", fg="#555555").grid(row=10, column=4, padx=3, pady=1)
Label(frame, text="Click Exit to close the app", bg="#1d1d1d", fg="#555555").grid(row=11, column=3, padx=3, pady=1)

# Define functions for buttons

def open_file(): 
    os.system('explorer')

def open_chrome():
    os.system('start chrome')

def open_settings():
    os.system('start ms-settings:')

def open_store():
    os.system('start ms-windows-store:')

def open_vlc():
    os.system('start vlc')

def open_excel():
    os.system('start excel')

def open_vscode():
    os.system('code')

def open_notepad():
    os.system('start notepad')

def open_calculator():
    os.system('start calc')

def open_taskmanager():
    os.system('start taskmgr')

def open_photos():
    os.system('start ms-photos:')

def open_cmd():
    os.system('start cmd')

def Exit():
    root.destroy()
 
# Buttons!
  
# Left Side

button_1 = tk.Button(frame, text="Files", padx=45, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_file)
button_1.grid(row=4, column=1, padx=10, pady=10)

button_2 = tk.Button(frame, text="Chrome", padx=35, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_chrome)
button_2.grid(row=5, column=1, padx=10, pady=10)

button_3 = tk.Button(frame, text="Settings", padx=35, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_settings)
button_3.grid(row=6, column=1, padx=10, pady=10)

button_4 = tk.Button(frame, text="Microsoft Store", padx=16, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_store)
button_4.grid(row=7, column=1, padx=10, pady=10)

button_5 = tk.Button(frame, text="VLC", padx=46, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_vlc)
button_5.grid(row=8, column=1, padx=10, pady=10)

button_6 = tk.Button(frame, text="Microsoft Excel", padx=16, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_excel)
button_6.grid(row=9, column=1, padx=10, pady=10)

# Right Side

button_7 = tk.Button(frame, text="Visual Stuido Code", padx=10, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_vscode)
button_7.grid(row=4, column=5, padx=10, pady=10)

button_8 = tk.Button(frame, text="Notepad", padx=36, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_notepad)
button_8.grid(row=5, column=5, padx=10, pady=10)

button_9 = tk.Button(frame, text="Calculator", padx=32, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_calculator)
button_9.grid(row=6, column=5, padx=10, pady=10)

button_10 = tk.Button(frame, text="Task Manager", padx=22, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_taskmanager)
button_10.grid(row=7, column=5, padx=10, pady=10)

button_11 = tk.Button(frame, text="Photos", padx=41, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=open_photos)
button_11.grid(row=8, column=5, padx=10, pady=10)

button_12 = tk.Button(frame, text="CMD", padx=46, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d",command=open_cmd)
button_12.grid(row=9, column=5, padx=10, pady=10)

# Exit Button (In the middle on the bottom)

exit_button = tk.Button(frame, text="Exit", padx=50, pady=10, fg="#1d1d1d", bg="#555555", activebackground="#555555", activeforeground="#1d1d1d", command=Exit)
exit_button.grid(row=10, column=3, padx=10, pady=10)

root.mainloop()

# End of code



