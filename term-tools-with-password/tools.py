#!/usr/bin/env python3

import os

# What do you want to do?

print() 

os.system('echo What would you like to do?')

print()

# Choose command(s) to execute 

os.system('\necho Choose a command:')

print('-----------------')

# Lists options for commands or exit 

os.system('\necho uuar: maintenance; \necho sdh: shutdown -h; \necho sdr: shutdown -r; \necho i: sudo apt install; \necho lsla: ls -la; \necho tp: top; \necho ht: htop; \necho ur: uname -r; \necho hnctl: hostnamectl; \necho lctl: localectl; \necho tdctl: timedatectl; \necho utp: uptime -p; \necho fh: free -h; \necho password: passwd; \necho ifc: ifconfig; \necho ipa: ip a; \necho ping: ping; \necho tr: traceroute; \necho nm: nmap; \necho ws: wireshark; \necho jr: john the ripper')

# Prompts user to enter a command

command = input('\nEnter a command: ')

# updates, upgrades, and removes packages no longer needed

if command == 'uua':
    os.system('sudo apt update && sudo apt upgrade; sudo apt autoremove')

# Shutdown System

if command == 'sdh':
    minutes = input('Enter minutes: ')
    os.system('shutdown -h ' + minutes)

# Reboot System

if command == "sdr":
    minutes = input("Enter minutes: ")
    os.system('shutdown -r ' + minutes)

# Install a package

if command == 'i':
    package = input('Enter package to install: ')
    os.system('sudo apt install ' + package)
    
# Run ls command for a directory

if command == 'lsla':
    directory = input('Enter directory to see contents of it: ')
    os.system('ls -la ' + directory)

# Run top
    
if command == 'tp':
    os.system('top')

# Run / install htop
 
if command == 'ht':
    os.system('htop')
    os.system('sudo apt install htop')
    os.system('clear')
        
# Run uname -r

if command == 'ur':
    os.system('uname -r')

# Run hostnamectl

if command == 'hnctl':
    os.system('hostnamectl')
    
# Run localectl

if command == 'lctl':
    os.system('localectl')
    
# Run timedatectl

if command == 'tdctl':
    os.system('timedatectl')

# Run uptime -p

if command == 'utp':
    os.system('uptime -p')
    
# Run free

if command == 'fh':
    os.system('free -h')

# Run passwd

if command == 'password':
    user = input('Enter user: ')
    os.system('passwd ' + user)
    
# Run ifconfig 

if command == 'ifc':
    os.system('ifconfig')
    
# Run ip a

if command == 'ipa':
    os.system('ip a')
        
# Run ping
    
if command == 'ping':
    address = input("Enter ip address: ")
    os.system('ping ' + address)
    
# Run traceroute

if command == 'tr':
    address = input("Enter ip address: ")
    os.system('traceroute ' + address)

# Run / install nmap
    
if command == 'nm':
    os.system('sudo apt install nmap')
    os.system('clear')
    command = input("Enter nmap command: ")
    os.system(command)
    
# Example - sudo nmap -sV -O scanme.nmap.org

# Run / install wirshark
    
if command == 'ws':
    os.system('wireshark &')
    os.system('sudo apt install wireshark')
    os.system('clear')
    os.system('wireshark &')
    	  
# Run / install john the ripper
    
if command == 'jr':
    os.system('sudo apt install john')
    os.system('clear')
    os.system('zip2john password.zip')
    os.system('zip2john password.zip > hash.txt')
    os.system('john --format=zip hash.txt')
    os.system('rm hash.txt')
    print('\nGood job hacking!')
    
else:
    print('\nHave a good day!')
    
# End of code
