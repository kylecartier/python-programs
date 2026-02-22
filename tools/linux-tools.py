#!/usr/bin/env python3

import os

# Welcome!

print() 

os.system('echo Welcome!')

print()

# Linux Tools

os.system('\necho Linux Tools')

print('-------------------------------------')

# Lists options or exit 

os.system('\necho 1. Administration Tools; \necho 2. Files and Directories; \necho 3. Networking Tools; \necho 4. Security Tools; \necho ; \necho Need some help?; \necho -------------------------------------; \necho 0. Man Page')

# Prompts user to enter a category or exit

category = input('\nChoose an option: ')

if category == '1':
    print('\nAdministration Tools')
    print('-------------------------------------')
    print('1.  df')
    print('2.  echo')
    print('3.  free')
    print('4.  hostnamectl')
    print('5.  htop')
    print('6.  id')
    print('7.  maintenance')
    print('8.  localectl')
    print('9.  ls')
    print('10. package management')
    print('11. pwd')
    print('12. reboot system')
    print('13. shutdown system')
    print('14. systemctl')
    print('15. timedatectl')
    print('16. top')
    print('17. uname')
    print('18. uptime')
    print('19. user accounts')
    print('20. whoami')
    
    admin_tool = input('\nChoose an option: ')
        
    if admin_tool == '1':
        flag = input('Enter df flag: ')
        os.system('df ' + flag)

    if admin_tool == '2':
        echo_command = input('Enter echo command: ')
        os.system('echo ' + echo_command)
         
    if admin_tool == '3':
        flag = input('Enter free flag: ')
        os.system('free ' + flag)
        
    if admin_tool == '4':
        os.system('hostnamectl')
        
    if admin_tool == '5':
        os.system('htop')

    if admin_tool == '6':
        flag = input('Enter id flag: ')
        os.system('id ' + flag)
        
    if admin_tool == '7':
        print('\nPackage Managers')
        print('-------------------------------------')
        print('1. apt')
        print('2. dnf')
        print('3. pacman')
       
        package_manager = input('\nEnter package manager: ')
        
        if package_manager == '1':
            os.system('sudo apt update && sudo apt upgrade; sudo apt autoremove')

        if package_manager == '2':
            os.system('sudo dnf update && sudo dnf autoremove')

        if package_manager == '3':
            os.system('sudo pacman -Syu')
        
    if admin_tool == '8':
        os.system('localectl')
        
    if admin_tool == '9':
        print('\nCommands')
        print('-------------------------------------')
        print('1. ls')
        print('2. lsblk')
        print('3. lscpu')
        print('4. lshw')
        print('5. lsmem')
        print('6. lsmod')
        print('7. lspci')
        print('8. lsusb')
        
        ls_command = input('\nChoose an option: ')
        
        if ls_command == '1':
            flag = input('Enter ls flag: ')
            directory = input('Enter directory to see contents of it: ') 
            if directory != '':
                os.system('ls ' + flag + ' ' + directory + '/')
            else:
                os.system('ls' + flag)
            
        if ls_command == '2':
            flag = input('Enter lsblk flag: ')
            if flag != '':
                os.system('lsblk' + ' ' + flag)
            else:
                os.system('lsblk')
                    
        if ls_command == '3':
            flag = input('Enter lscpu flag: ')
            if flag != '':
                os.system('lscpu' + ' ' + flag)
            else:
                os.system('lscpu')
                
        if ls_command == '4':
            flag = input('Enter lshw flag: ')
            if flag != '':
                os.system('lshw' + ' ' + flag)
            else:
                os.system('lshw')
                    
        if ls_command == '5':
            flag = input('Enter lsmem flag: ')
            if flag != '':
                os.system('lsmem' + ' ' + flag)
            else:
                os.system('lsmem')
                
        if ls_command == '6':
            os.system('lsmod')
                          
        if ls_command == '7':
            flag = input('Enter lspci flag: ')
            if flag != '':
                os.system('lspci' + ' ' + flag)
            else:
                os.system('lspci')
                    
        if ls_command == '8':
            flag = input('Enter lsusb flag: ')
            if flag != '':
                os.system('lsusb' + ' ' + flag)
            else:
                os.system('lsusb')
                
    if admin_tool == '10':
        print('\nPackage Managers')
        print('-------------------------------------')
        print('1. apt')
        print('2. dnf')
        print('3. pacman')
        
        package_manager = input('\nEnter package manager: ')
        package = input('Enter name of package: ')
        command = input('Want to install or remove package?: ')
        
        if package_manager == '1':
            if command == 'install':
                os.system('sudo apt install ' + package)
            if command == 'remove':
                os.system('sudo apt remove ' + package)

        if package_manager == '2':
            if command == 'install':
                os.system('sudo dnf install ' + package)
            if command == 'remove':
                os.system('sudo dnf remove ' + package)

        if package_manager == '3':
            if command == 'install':
                os.system('sudo pacman -S ' + package)
            if command == 'remove':
                os.system('sudo pacman -Rns ' + package)

    if admin_tool == '11':
        os.system('pwd')
        
    if admin_tool == '12':
        minutes = input("Enter minutes: ")
        if minutes != '':
            os.system('shutdown -r ' + minutes)
        else:
            os.system('reboot now')
        
    if admin_tool == '13':
        minutes = input('Enter minutes: ')
        if minutes != '':
            os.system('shutdown -h ' + minutes)
        else:
            os.system('shutdown now')
        
    if admin_tool == '14':
        service = input('Enter service: ')
        command = input('Enter command: ')
        if service != '' and command == 'is-active':
            os.system('sudo systemctl ' + command + ' ' + service)
        if service != '' and command == 'is-enabled':
            os.system('sudo systemctl ' + command + ' ' + service)
        if service == '' and command == '':
            os.system('systemctl --version')
        else:
            exit(0)
        
    if admin_tool == '15':
        os.system('timedatectl')
        
    if admin_tool == '16':
        os.system('top')

    if admin_tool == '17':
        flag = input('Enter uname flag: ')
        os.system('uname ' + flag)

    if admin_tool == '18':
        flag = input('Enter uptime flag: ')
        os.system('uptime ' + flag)

    if admin_tool == '19':
        print('\nCommands')
        print('-------------------------------------')
        print('1. change password for user account')
        print('2. lock user account')
        print('3. switch to another user account')
        print('4. unlock user account')

        user_command = input('\nChoose an option: ')

        if user_command == '1':
            user = input('Enter user: ')
            if user == '' or 'root':
                os.system('passwd root')
            else:
                os.system('passwd ' + user)

        if user_command == '2':
            user = input('Enter user: ')
            if user == '' or 'root':
                os.system('sudo usermod -L root')
            else:
                os.system('sudo usermod -L ' + user)

        if user_command == '3':
            user = input('Enter user: ')
            if user == '' or 'root':
                os.system('su')
            else:
                os.system('su ' + user)

        if user_command == '4':
            user = input('Enter user: ')
            if user == '' or 'root':
                os.system('sudo usermod -L root')
            else:
                os.system('sudo usermod -L ' + user)

    if admin_tool == '20':
        os.system('whoami')
        
if category == '2':
    print('\nFiles and Directories')
    print('-------------------------------------')
    print('1. add and delete files ')
    print('2. add and delete directories')
    print('3. make files executable and not executable')
    print('4. read files')
    print('5. text editors')
    
    files_command = input('\nChoose an option: ')
    
    if files_command == '1':
        print('\nCommands')
        print('-------------------------------------')
        print('1. add files')
        print('2. delete files')
        
        add_or_del_files = input('\nChoose an option: ')
        
        if add_or_del_files == '1':
            file = input('Enter file to modify: ')
            os.system('touch' + ' ' + file)
        
        if add_or_del_files == '2':
            file = input('Enter file to modify: ')
            os.system('rm' + ' ' + file)
                
    if files_command == '2':
        print('\nCommands')
        print('-------------------------------------')
        print('1. add directories')
        print('2. delete directories')
        
        add_or_del_folders = input('\nChoose an option: ')
        
        if add_or_del_folders == '1':
            folder = input('Enter folder to modify: ')
            os.system('mkdir ' + folder + '/')
    
        if add_or_del_folders == '2':
            folder = input('Enter folder to modify: ')
            empty = input('Is the folder empty: ')
            if empty == 'no':
                os.system('rm -r ' + folder + '/')
            if empty == 'yes':
                os.system('rmdir ' + folder + '/')
                
    if files_command == '3':
        print('\nCommands')
        print('-------------------------------------')
        print('1. make files executable')
        print('2. make files not executable')
        
        files_execute_command = input('\nChoose an option: ')
        
        if files_execute_command == '1':
            file = input('Enter file to modify: ')
            command = input('Enter command: ')
            if command == 'chmod +x':
                os.system(command + ' ' + file)
            
        if files_execute_command == '2':
            file = input('Enter file to modify: ')
            command = input('Enter command: ')
            if command == 'chmod -x':
                os.system(command + ' ' + file)     
                
    if files_command == '4':
        file = input('Enter file to read it: ')
        command = input('Enter command: ')
        if command == 'cat':
            os.system(command + ' ' + file)

    if files_command == '5':
        print('\nCommands')
        print('-------------------------------------')
        print('1. nano')
        print('2. vi')
        print('3. vim') 
        
        editor_command = input('\nChoose an option: ')

        if editor_command == '1':
            file = input('Enter file to edit it: ')
            if file != '':
                os.system('nano ' + file)

        if editor_command == '2':
            file = input('Enter file to edit it: ')
            if file != '':
                os.system('vi ' + file)

        if editor_command == '3':
            file = input('Enter file to edit it: ')
            if file != '':
                os.system('vi ' + file)
      
if category == '3':
    print('\nNetworking Tools')
    print('-------------------------------------')
    print('1.  arp')
    print('2.  dig')
    print('3.  ifconfig')
    print('4.  ip a')
    print('5.  netstat')
    print('6.  nmap')
    print('7.  nslookup')
    print('8.  ping')
    print('9.  tcpdump')
    print('10. traceroute')
    
    network_tool = input('\nChoose an option: ')
    
    if network_tool == '1':
        flag = input('Enter arp flag: ')
        os.system('arp ' + flag)
        
    if network_tool == '2':
        url = input("Enter url: ")
        os.system('dig ' + url)
            
    if network_tool == '3':
        os.system('ifconfig')
     
    if network_tool == '4':
        os.system('ip a')
        
    if network_tool == '5':
        flag = input('Enter netstat flag: ')
        os.system('netstat ' + flag)
        
    if network_tool == '6':
        nmap_command = input('Enter nmap commnad: ')
        os.system(nmap_command)
        
    if network_tool == '7':
        url = input("Enter url: ")
        os.system('nslookup ' + url)
        
    if network_tool == '8':
        address = input("Enter ip address: ")
        packet_num = input('How many packets to capture?: ')
        if packet_num != '':
            os.system('ping -c ' + packet_num + ' ' + address)
        else:
            os.system('ping ' + address)
        
    if network_tool == '9':
        interface = input('Enter network interface: ')
        if interface == '':
            os.system('sudo tcpdump -D')
        else:
            os.system('sudo tcpdump -i ' + interface)
        
    if network_tool == '10':
        address = input("Enter ip address: ")
        os.system('traceroute ' + address)
            
if category == '4':
    print('\nSecurity Tools')
    print('-------------------------------------')
    print('1. ufw (gufw too!)')
    



    security_tool = input('\nChoose an option: ')
    
    if security_tool == '1':
        print('\nCommands')
        print('--------------------------------------')
        print('1. allow, deny, limit, and reject rules')
        print('2. identify ufw status')
        print('3. install ufw')
        print('4. install gufw (graphical ufw)')
        
        ufw_command = input('\nChoose an option: ')
        
        if ufw_command == '1':
            rule = input('Enter a rule to modify: ')
            command = input('Want to allow, deny, limit, or reject the firewall rule?: ')
            if command == 'allow':
                os.system('sudo ufw allow ' + rule)
                
            if command == 'deny':
                os.system('sudo ufw deny ' + rule)
                
            if command == 'limit':
                os.system('sudo ufw limit ' + rule)
                
            if command == 'reject':
                os.system('sudo ufw reject ' + rule)
                
            else:
                exit(0)
            
        if ufw_command == '2':
            numbers_command = input('Show in numbered format?: ')
            if numbers_command == 'y':
                os.system('sudo ufw status numbered')
                
            if numbers_command == 'n':
                os.system('sudo ufw status')
                
            else:
                exit(0)
                
        if ufw_command == '3':
            print('\nPackage Managers')
            print('-------------------------------------')
            print('1. apt')
            print('2. dnf')
            print('3. pacman')
       
            package_manager = input('\nEnter package manager: ')
        
            if package_manager == '1':
                os.system('sudo apt install ufw')

            if package_manager == '2':
                os.system('sudo dnf install ufw')

            if package_manager == '3':
                os.system('sudo pacman -S ufw')
            
        if ufw_command == '4':
            print('\nPackage Managers')
            print('-------------------------------------')
            print('1. apt')
            print('2. dnf')
            print('3. pacman')
       
            package_manager = input('\nEnter package manager: ')
        
            if package_manager == '1':
                os.system('sudo apt install gufw')

            if package_manager == '2':
                os.system('sudo dnf install gufw')

            if package_manager == '3':
                os.system('sudo pacman -S gufw')
            
if category == '0':

    command_list = ('passwd', 'usermod', 'sudo', 'su', 'df', 'free', 'echo', 'id', 'hostnamectl', 'htop', 'apt', 'dnf', 'pacman', 'install', 'remove', 'localectl', 'ls', 'lsblk', 'ls', 'lsblk', 'lscpu', 'lshw', 'lsmem', 'lsmod', 'lspci', 'lsusb', 'pwd', 'shutdown', 'systemctl', 'timedatectl', 'top', 'touch', 'rm', 'rmdir', 'chmod', 'cat', 'ufw', 'gufw', 'arp', 'dig', 'ifconfig', 'ip', 'netstat', 'nmap', 'nslookup', 'ping', 'tcpdump', 'traceroute', 'nano', 'vi', 'vim')
    
    command = input('Enter command to need help with?: ')
    if command in command_list:
        os.system('man' + ' ' + command)

else:
    exit(0)

# End of Code
