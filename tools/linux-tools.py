#!/usr/bin/env python3

import os

# What do you want to do?

print() 

os.system('echo What would you like to do?')

print()

# Choose tool category to execute 

os.system('\necho Choose a tool category: ')

print('-----------------------')

# Lists options for tools or exit 

os.system('\necho 1. Administration Tools; \n echo 2. Networking Tools; \necho 3. Security Tools')

# Prompts user to enter a command

category = input('\nEnter a tool category to continue: ')

if category == '1':
    print('\nAdministration Tools')
    print('--------------------')
    print('1.  change password')
    print('2.  free')
    print('3.  hostnamectl')
    print('4.  htop')
    print('5.  install package(s)')
    print('6.  localectl')
    print('7.  ls')
    print('8.  maintenance')
    print('9.  pwd')
    print('10. reboot system')
    print('11. shutdown system')
    print('12. systemctl')
    print('13. timedatectl')
    print('14. top')
    print('15. uname')
    print('16. uptime')
    print('17. whoami')
    
    admin_tool = input('\nChoose a tool to run: ')
    
    if admin_tool == '1':
        user = input('Enter user: ')
        os.system('passwd ' + user)
         
    if admin_tool == '2':
        flag = input('Enter free flag: ')
        os.system('free ' + flag)
        
    if admin_tool == '3':
        os.system('hostnamectl')
        
    if admin_tool == '4':
        os.system('htop')
        
    if admin_tool == '5':
        package = input('Enter package to install: ')
        os.system('sudo apt install ' + package)
        
    if admin_tool == '6':
        os.system('localectl')
        
    if admin_tool == '7':
        flag = input('Enter ls flag: ')
        directory = input('Enter directory to see contents of it: ') 
        if directory != '':
            os.system('ls ' + flag + ' ' + directory + '/')
        else:
            os.system('ls' + flag)

    if admin_tool == '8':
        os.system('sudo apt update && sudo apt upgrade; sudo apt autoremove')
        
    if admin_tool == '9':
        os.system('pwd')
        
    if admin_tool == '10':
        minutes = input("Enter minutes: ")
        os.system('shutdown -r ' + minutes)
        
    if admin_tool == '11':
        minutes = input('Enter minutes: ')
        os.system('shutdown -h ' + minutes)
        
    if admin_tool == '12':
        service = input('Enter service: ')
        command = input('Enter command: ')
        os.system('sudo systemctl ' + command + ' ' + service)
        
    if admin_tool == '13':
        os.system('timedatectl')
        
    if admin_tool == '14':
        os.system('top')

    if admin_tool == '15':
        flag = input('Enter uname flag: ')
        os.system('uname ' + flag)

    if admin_tool == '16':
        flag = input('Enter uptime flag: ')
        os.system('uptime ' + flag)

    if admin_tool == '17':
        os.system('whoami')

if category == '2':
    print('\nNetworking Tools')
    print('----------------')
    print('1. arp')
    print('2. ifconfig')
    print('3. ip a')
    print('4. nmap')
    print('5. netstat')
    print('6. ping')
    print('7. traceroute')
    
    network_tool = input('\nChoose a tool to run: ')
    
    if network_tool == '1':
        flag = input('Enter arp flag: ')
        os.system('arp ' + flag)
            
    if network_tool == '2':
        os.system('ifconfig')
     
    if network_tool == '3':
        os.system('ip a')
        
    if network_tool == '4':
        nmap_command = input('Enter nmap commnad: ')
        os.system(nmap_command)
        
    if network_tool == '5':
        os.system('netstat')
        
    if network_tool == '6':
        address = input("Enter ip address: ")
        os.system('ping ' + address)
        
    if network_tool == '7':
        address = input("Enter ip address: ")
        os.system('traceroute ' + address)
            
if category == '3':
    print('\nSecurity Tools')
    print('--------------')
    
    security_tool = input('\nChoose a tool to run:  ')
    

else:
    exit(0)

# End of Code
