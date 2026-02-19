#!/usr/bin/env python3

import os

# Rofi Launcher!

# What do you want to do?

print() 

os.system('echo What would you like to do?')

print()

# Choose command to execute 

os.system('\necho Choose a command:')

print('-----------------')

# Lists options for commands or exit

os.system('\necho 1. install rofi on debian based systems; \necho 2. install rofi on rhel based systems; \necho 3. install rofi on arch based systems; \necho 4. launch rofi theme selector; \necho 5. launch rofi showing all applications on the system; \necho 6. launch rofi showing all files on the system; \necho 7. launch rofi showing all open windows on the system; \necho 8. uninstall rofi on debian based systems; \necho 9. uninstall rofi on rhel based systems; \necho 10. uninstall rofi on arch based systems')

# Prompt user to install rofi, launch rofi for applications, files, and any open windows, change rofi theme, or uninstall rofi

command = input('\nEnter a command: ')

# Install rofi if it's not installed  (Debian, RHEL, or Arch based distributions)

if command == '1':
    os.system('sudo apt install rofi -y')

if command == '2':
    os.system('sudo dnf install rofi -y')

if command == '3':
    os.system('sudo pacman -S rofi -y')
    
# Launch rofi theme selector

if command == '4':
    os.system('rofi-theme-selector')

# Launch rofi (applications, files, and open windows on the system)

if command == '5':
    os.system('rofi -show drun -show-icons')

if command == '6':
    os.system('rofi -show filebrowser -show-icons')
    
if command == '7':
    os.system('rofi -show window -show-icons')

# Uninstall rofi (Debian, RHEL, or Arch based distributions)

if command == '8':
    os.system('sudo apt remove rofi -y')

if command == '9':
    os.system('sudo dnf remove rofi -y')

if command == '10':
    os.system('sudo pacman -Rns rofi -y')

# Once the program is finished executing
    
else:
    print('\nHave a good day!')

# End of Code
