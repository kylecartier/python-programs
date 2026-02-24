#!/usr/bin/env python3

import os

# Timeshift

# Welcome!

print() 

os.system('echo Welcome!')

print()

# Choose command to execute 

os.system('\necho Timeshift')

print('-------------------------------------')

# Lists options for commands or exit

os.system('\necho 1. Installation; \necho 2. Options; \necho 3. Uninstall; \necho ; \necho Need some help?; \necho -------------------------------------; \necho 0. Man Page')

# Prompt user to install timeshift, lists options for timeshift once installed. and uninstall timeshift

timeshift_command = input('\nChoose an option: ')

if timeshift_command == '1':
    print('\nInstallation')
    print('-------------------------------------')
    print('1. installation on arch system')
    print('2. installation on debian system')
    print('3. installation on rhel system')
    
    install_command = input('\nChoose an option: ')
    
    if install_command == '1':
        os.system('sudo pacman -S timeshift -y')
        
    if install_command == '2':    
        os.system('sudo apt install timeshift -y')
    
    if install_command == '3':
        os.system('sudo dnf install timeshift -y')
        
if timeshift_command == '2':
    print('\nOptions')
    print('-------------------------------------')
    print('1. check timeshift status')
    print('2. delete snapshots')
    print('3. list snapshots')
    print('4. show timeshift version')
    
    options_command = input('\nChoose an option: ')
    
    if options_command == '1':
        os.system('sudo timeshift --check')
        
    if options_command == '2':
        print('\nCommands')
        print('-------------------------------------')
        print('1. delete a snapshot')
        print('2. delete all snapshots')
        
        delete_command = input('\nChoose an option: ')
        
        if delete_command == '1':
                os.system('sudo timeshift --delete')
                
        if delete_command == '2':
            os.system('sudo timeshift --delete-all')
    
    if options_command == '3':
        os.system('sudo timeshift --list')
        
    if options_command == '4':
        os.system('timeshift --version')
        
if timeshift_command == '3':
    print('\nUninstall')
    print('-------------------------------------')
    print('1. uninstall on arch system')
    print('2. uninstall on debian system')
    print('3. uninstall on rhel system')

    uninstall_command = input('\nChoose an option: ')
    
    if uninstall_command == '1':
        os.system('sudo pacman -Rns timeshift -y')

    if uninstall_command == '2':
        os.system('sudo apt remove timeshift -y')

    if uninstall_command == '3':
        os.system('sudo dnf remove timeshift -y')
        
if timeshift_command == '0':
    os.system('sudo timeshift')   

# Once the program is finished executing
    
else:
    exit(0)
        
# End of Code
