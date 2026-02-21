#!/usr/bin/env python3

import os

# Rofi Launcher!

# What do you want to do?

print() 

os.system('echo Welcome!')

print()

# Choose command to execute 

os.system('\necho Rofi Launcher')

print('-------------------------------------')

# Lists options for commands or exit

os.system('\necho 1. Installation; \necho 2. Options; \necho 3. Uninstall; \necho ; \necho Need some help?; \necho -------------------------------------; \necho 0. Man Page; \necho ; \necho Exit; \necho -------------------------------------; \necho Type Exit or exit to do so, thanks.')

# Prompt user to install rofi, launch rofi for applications, files, and any open windows, change rofi theme, or uninstall rofi

rofi_command = input('\nChoose an option: ')

# Install rofi if it's not installed  (Debian, RHEL, or Arch based distributions)

if rofi_command == '1':
    print('\nInstallation')
    print('-------------------------------------')
    print('1. installation on arch system')
    print('2. installation on debian system')
    print('3. installation on rhel system')
    
    install_command = input('\nChoose an option: ')
    
    if install_command == '1':
        os.system('sudo pacman -S rofi -y')
        
    if install_command == '2':    
        os.system('sudo apt install rofi -y')
    
    if install_command == '3':
        os.system('sudo dnf install rofi -y')
        
if rofi_command == '2':
    print('\nOptions')
    print('-------------------------------------')
    print('1. run rofi with icons')
    print('2. show open windows')
    print('3. theme selector')
    
    options_command = input('\nChoose an option: ')
    
    if options_command == '1':
        os.system('rofi -show drun -show-icons')
        
    if options_command == '2':
        os.system('rofi -show window -show-icons')
        
    if options_command == '3':
        os.system('rofi-theme-selector')
        
if rofi_command == '3':
    print('\nUninstall')
    print('-------------------------------------')
    print('1. uninstall on arch system')
    print('2. uninstall on debian system')
    print('3. uninstall on rhel system')

    uninstall_command = input('\nChoose an option: ')
    
    if uninstall_command == '1':
        os.system('sudo pacman -Rns rofi -y')

    if uninstall_command == '2':
        os.system('sudo apt remove rofi -y')

    if uninstall_command == '3':
        os.system('sudo dnf remove rofi -y')
        
if rofi_command == '0':
    os.system('man rofi')   

if rofi_command == 'Exit' or 'exit':
    exit(0)

# Once the program is finished executing
    
else:
    exit(0)

# End of Code
