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

# Administration Tools

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
        if flag != '':
            os.system('df ' + flag)
        else:
            os.system('df')

    if admin_tool == '2':
        echo_command = input('Enter echo command: ')
        os.system('echo ' + echo_command)
         
    if admin_tool == '3':
        flag = input('Enter free flag: ')
        if flag != '':
            os.system('free ' + flag)
        else:
            os.system('free')
        
    if admin_tool == '4':
        os.system('hostnamectl')
        
    if admin_tool == '5':
        flag = input('Enter htop flag: ')
        if flag != '':
            os.system('htop ' + flag)
        else:
            os.system('htop')

    if admin_tool == '6':
        print('\nCommands')
        print('-------------------------------------')
        print('1. blkid')
        print('2. id')
        
        id_command = input('\nChoose an option: ')
        
        if id_command == '1':
            flag = input('Enter blkid flag: ')
            if flag != '':
                os.system('blkid ' + flag)
            else:
                os.system('blkid')
        
        if id_command == '2':
            flag = input('Enter id flag: ')
            os.system('id ' + flag)
        
    if admin_tool == '7':
        print('\nCommands')
        print('-------------------------------------')
        print('1. dmesg')
        print('2. history')
        print('3. journalctl')
        print('4. ssh')
        print('5. update repositories, upgrade packages, and remove no longer needed packages')
        
        maintenance_command = input('\nChoose an option: ')
        
        if maintenance_command == '1':
            flag = input('Enter dmesg flag: ')
            if flag != '':
                os.system('sudo dmesg ' + flag)
            else:
                os.system('sudo dmesg')
                
        if maintenance_command == '2':
            os.system('cat -n ~/.bash_history')
            
        if maintenance_command == '3':
            flag = input('Enter journalctl flag: ')
            service = input('Enter service: ')
            if flag != '' and service != '':
                os.system('journalctl ' + flag + ' ' + service)
            
            if flag != '' and service == '':
                os.system('journalctl ' + flag)
                
            if flag == '' and service == '':
                os.system('journalctl')

        if maintenance_command == '4':
            print('\nCommands')
            print('-------------------------------------')
            print('1. disable ssh')
            print('2. enable ssh')
            print('3. identify status of ssh')
            print('4. install ssh')
            print('5. run ssh')
            print('6. start ssh')
            print('7. stop ssh')
            
            ssh_command = input('\nChoose an option: ')
            
            if ssh_command == '1':
                os.system('sudo systemctl disable ssh')
            
            if ssh_command == '2':
                os.system('sudo systemctl enable ssh')
                
            if ssh_command == '3':
                os.system('sudo systemctl is-active ssh')
                os.system('sudo systemctl is-enabled ssh')
                
            if ssh_command == '4':
                print('\nPackage Managers')
                print('-------------------------------------')
                print('1. apt')
                print('2. dnf')
                print('3. pacman')
               
                package_manager = input('\nEnter package manager: ')
                
                if package_manager == '1':
                    os.system('sudo apt install ssh')

                if package_manager == '2':
                    os.system('sudo dnf install ssh')

                if package_manager == '3':
                    os.system('sudo pacman -S ssh')
            
            if ssh_command == '5':
                username = input('What is the username?: ')
                ip_address = input('What is the ip address?: ')
                if username != '' and ip_address != '':
                    os.system('ssh ' + username + '@' + ip_address)
                else:
                    exit(0)
                    
            if ssh_command == '6':
                os.system('sudo systemctl start ssh')
                
            if ssh_command == '7':
                os.system('sudo systemctl stop ssh')

        if maintenance_command == '5':
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
            os.system('sudo systemctl is-active ' + service)
        if service != '' and command == 'is-enabled':
            os.system('sudo systemctl is-enabled ' + service)
        if service != '' and command == 'start':
            os.system('sudo systemctl start ' + service)
        if service != '' and command == 'stop':
            os.system('sudo systemctl stop ' + service)
        if service != '' and command == 'restart':
            os.system('sudo systemctl restart ' + service)
        if service != '' and command == 'reload':
            os.system('sudo systemctl reload ' + service)
        if service == '' and command == '':
            os.system('systemd --version')
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
        flag = input('Enter whoami flag: ')
        if flag == '--version':
            os.system('whoami ' + flag)
        else:
            os.system('whoami')
        
# Files and Directories
        
if category == '2':
    print('\nFiles and Directories')
    print('-------------------------------------')
    print('1. add and delete files ')
    print('2. add and delete directories')
    print('3. make files executable and not executable')
    print('4. read files')
    print('5. text editors')
    print('6. tree')
    
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
        flag = input('Enter cat flag: ')
        if flag != '' and file != '':
            os.system('cat ' + flag + ' ' + file)
        if flag == '' and file != '':
            os.system('cat ' + file)
        if flag == '' and file == '':
            exit(0)
    
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
                os.system('vim ' + file)
                
    if files_command == '6':
        flag = input('Enter tree flag: ')
        directory = input('Enter directory: ')
        if flag == '':
            os.system('tree ' + directory)
        
        if directory and flag != '':
            os.system('tree ' + flag + ' ' + directory)
        
        else:
            exit(0)
            
# Networking Tools
      
if category == '3':
    print('\nNetworking Tools')
    print('-------------------------------------')
    print('1.  arp')
    print('2.  dig')
    print('3.  ifconfig')
    print('4.  ip addr')
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
        os.system('ip addr')
        
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
        flag = input('Enter tcpdump flag: ')
        interface = input('Enter network interface: ')
        if flag and interface != '':
            os.system('sudo tcpdump ' + flag + ' ' + interface)
            
        if flag != '' and interface == '':
            os.system('sudo tcpdump ' + flag)
        
        else:
            exit(0)
        
    if network_tool == '10':
        address = input("Enter ip address: ")
        os.system('traceroute ' + address)
        
# Security Tools
            
if category == '4':
    print('\nSecurity Tools')
    print('-------------------------------------')
    print('1. Defensive Tools')
    print('2. Offensive Tools')

    tools = input('\nChoose an option: ')

    if tools == '1':
        print('\nDefensive Tools')
        print('-------------------------------------')
        print('1. firewalls')
        
        defensive_tool = input('\nChoose an option: ')
        
        if defensive_tool == '1':
        
            print('\nfirewalls')
            print('-------------------------------------')
            print('1. firewalld')
            print('2. iptables')
            print('3. ufw (gufw too!)')
            
            ufw_option = input('\nChoose an option: ')
            
            if ufw_option == '3':
                print('\nCommands')
                print('--------------------------------------')
                print('1. allow, deny, limit, and reject rules')
                print('2. enable ufw')
                print('3. disable ufw')
                print('4. identify ufw status')
                print('5. install ufw')
                print('6. install gufw (graphical ufw)')
                
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
                    os.system('sudo ufw enable')
                    
                if ufw_command == '3':
                    os.system('sudo ufw disable')
                    
                if ufw_command == '4':
                    numbers_command = input('Show in numbered format?: ')
                    if numbers_command == 'y':
                        os.system('sudo systemctl is-enabled ufw')
                        os.system('sudo ufw status numbered')
                        
                    if numbers_command == 'n':
                        os.system('sudo systemctl is-enabled ufw')
                        os.system('sudo ufw status')
                        
                    else:
                        exit(0)
                        
                if ufw_command == '5':
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
                    
                if ufw_command == '6':
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
                        
    if tools == '2':
        print('\nOffensive Tools')
        print('-------------------------------------')
        print('1. ')
    
        offensive_tool = input('\nChoose an option: ')
        
        if offensive_tool == '1':
            
                    
# Need some help?
            
if category == '0':

    command_list = ('passwd', 'usermod', 'sudo', 'su', 'df', 'free', 'echo', 'id', 'hostnamectl', 'htop', 'apt', 'dnf', 'pacman', 'install', 'remove', 'localectl', 'ls', 'lsblk', 'ls', 'lsblk', 'lscpu', 'lshw', 'lsmem', 'lsmod', 'lspci', 'lsusb', 'pwd', 'shutdown', 'systemctl', 'timedatectl', 'top', 'touch', 'rm', 'rmdir', 'chmod', 'cat', 'ufw', 'gufw', 'arp', 'dig', 'ifconfig', 'ip', 'netstat', 'nmap', 'nslookup', 'ping', 'tcpdump', 'traceroute', 'nano', 'vi', 'vim', 'tree', 'dmesg', 'journalctl', 'history', 'blkid', 'firewalld', 'iptables', 'ssh')
    
    command = input('Enter command to need help with?: ')
    if command in command_list:
        os.system('man' + ' ' + command)

else:
    exit(0)

# End of Code
