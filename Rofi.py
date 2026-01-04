#!/usr/bin/env python3

import os

# Rofi Launcher!

# Prompt user to install rofi, launch rofi, change rofi theme, or uninstall rofi 

command = (input("Enter the command to launch rofi or change its theme: "))

# Install rofi if it's not installed  (Debian, RHEL, and Arch based distributions)

if command == 'ird':
    os.system('sudo apt install rofi')

if command == 'irr':
    os.system('sudo dnf install rofi')

if command == 'ira':
    os.system('sudo pacman -S rofi')

# If installed, launch rofi

if command == 'lr':
    os.system ('rofi -show drun -show-icons')

# Lauch the theme selector

if command == 'rts':
    os.system('rofi-theme-selector')

# Uninstall rofi (Debian, RHEL, and Arch based distributions)

if command == 'urd':
    os.system('sudo apt remove rofi')

if command == 'urr':
    os.system('sudo dnf remove rofi')

if command == 'ura':
    os.system('sudo pacman -Rns rofi')

# End of Code
