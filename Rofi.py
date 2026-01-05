#!/usr/bin/env python3

import os

# Rofi Launcher!

# What do you want to do?

print() 

os.system('echo What would you like to do?')

print()

# Choose command(s) to execute 

os.system('\necho Choose a command:')

print('-----------------')

# Lists options for commands or exit

os.system('\necho ird: install rofi on debian based systems; \necho irr: install rofi on rhel based systems; \necho ira: install rofi on arch based systems; \necho lra: launch rofi showing all application on the system; \necho lrf: launch rofi showing all files on the system; \necho lrw: launch rofi showing any open windows on the system; \necho rts: rofi theme selector; \necho urd: uninstall rofi on debian based systems; \necho urr: uninstall rofi on rhel based systems; \necho ura: uninstall rofi on arch based systems')

# Prompt user to install rofi, launch rofi for applications, files, and any open windows, change rofi theme, or uninstall rofi

command = input('\nEnter a command: ')

# Install rofi if it's not installed  (Debian, RHEL, or Arch based distributions)

if command == 'ird':
    os.system('sudo apt install rofi')

if command == 'irr':
    os.system('sudo dnf install rofi')

if command == 'ira':
    os.system('sudo pacman -S rofi')

# If installed, launch rofi (applications, files, and open windows on the system)

if command == 'lra':
    os.system('rofi -show drun -show-icons')

if command == 'lrf':
    os.system('rofi -show filebrowser -show-icons')
    
if command == 'lrw':
    os.system('rofi -show window -show-icons')

# Lauch the theme selector

if command == 'rts':
    os.system('rofi-theme-selector')

# Uninstall rofi (Debian, RHEL, or Arch based distributions)

if command == 'urd':
    os.system('sudo apt remove rofi')

if command == 'urr':
    os.system('sudo dnf remove rofi')

if command == 'ura':
    os.system('sudo pacman -R rofi')
    
else:
    print('\nHave a good day!')

# End of Code
