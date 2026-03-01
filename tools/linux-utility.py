#!/usr/bin/env python3

import os

# Welcome!

# Linux Utility

# Lists options or exit 

print() 

print('---------------------------------------------------')
print('-                                                 -')
print('-                    Welcome!                     -')
print('-                                                 -')
print('-                 Linux Utility                   -')
print('-                                                 -')
print('-                  Categories                     -')
print('- ----------------------------------------------- -')
print('-             1. Administration Tools             -')
print('-             2. Files and Directories            -')
print('-             3. Networking Tools                 -')
print('-             4. Security Tools                   -')
print('-                                                 -')
print('-                Need some help?                  -')
print('- ----------------------------------------------- -')
print('-             0. Man Page                         -')
print('-                                                 -')
print('---------------------------------------------------')

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
        print('5. timeshift')
        print('6. update repositories, upgrade packages, and remove no longer needed packages')
        
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
            print('\nCommands')
            print('-------------------------------------')
            print('1. Installation')
            print('2. Options')
            print('3. Uninstall')
            
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

        if maintenance_command == '6':
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
            if flag == '':
                os.system('ls ' + directory)
            else:
                os.system('ls ' + flag)
            
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
        print('\nCommands')
        print('-------------------------------------')
        print('1. disable ntp')
        print('2. enable ntp')
        print('3. list timezones')
        print('4. set timezone')
        
        tdctl = input('\nChoose an option: ')
        
        if tdctl == '1':
            os.system('timedatectl set-ntp false')
        if tdctl == '2':
            os.system('timdatectl set-ntp true')
        if tdctl == '3':
            os.system('timedatectl list-timezones')
       
        timezones = (
                    'Africa/Abidjan' 
                    ,'Africa/Accra' 
                    ,'Africa/Abidjan'
                    ,'Africa/Accra'
                    ,'Africa/Addis_Ababa'
                    ,'Africa/Algiers'
                    ,'Africa/Asmara'
                    ,'Africa/Bamako'
                    ,'Africa/Bangui'
                    ,'Africa/Banjul'
                    ,'Africa/Bissau'
                    ,'Africa/Blantyre'
                    ,'Africa/Brazzaville'
                    ,'Africa/Bujumbura'
                    ,'Africa/Cairo'
                    ,'Africa/Casablanca'
                    ,'Africa/Ceuta'
                    ,'Africa/Conakry'
                    ,'Africa/Dakar'
                    ,'Africa/Dar_es_Salaam'
                    ,'Africa/Djibouti'
                    ,'Africa/Douala'
                    ,'Africa/El_Aaiun'
                    ,'Africa/Freetown'
                    ,'Africa/Gaborone'
                    ,'Africa/Harare'
                    ,'Africa/Johannesburg'
                    ,'Africa/Juba'
                    ,'Africa/Kampala'
                    ,'Africa/Khartoum'
                    ,'Africa/Kigali'
                    ,'Africa/Kinshasa'
                    ,'Africa/Lagos'
                    ,'Africa/Libreville'
                    ,'Africa/Lome'
                    ,'Africa/Luanda'
                    ,'Africa/Lubumbashi'
                    ,'Africa/Lusaka'
                    ,'Africa/Malabo'
                    ,'Africa/Maputo'
                    ,'Africa/Maseru'
                    ,'Africa/Mbabane'
                    ,'Africa/Mogadishu'
                    ,'Africa/Monrovia'
                    ,'Africa/Nairobi'
                    ,'Africa/Ndjamena'
                    ,'Africa/Niamey'
                    ,'Africa/Nouakchott'
                    ,'Africa/Ouagadougou'
                    ,'Africa/Porto-Novo'
                    ,'Africa/Sao_Tome'
                    ,'Africa/Timbuktu'
                    ,'Africa/Tripoli'
                    ,'Africa/Tunis' 
                    ,'Africa/Windhoek'
                    ,'America/Adak'
                    ,'America/Anchorage'
                    ,'America/Anguilla'
                    ,'America/Antigua'
                    ,'America/Araguaina'
                    ,'America/Argentina/Buenos_Aires'
                    ,'America/Argentina/Catamarca'
                    ,'America/Argentina/Cordoba'
                    ,'America/Argentina/Jujuy'
                    ,'America/Argentina/La_Rioja'
                    ,'America/Argentina/Mendoza'
                    ,'America/Argentina/Rio_Gallegos'
                    ,'America/Argentina/Salta'
                    ,'America/Argentina/San_Juan'
                    ,'America/Argentina/San_Luis'
                    ,'America/Argentina/Tucuman'
                    ,'America/Argentina/Ushuaia'
                    ,'America/Aruba'
                    ,'America/Asuncion'
                    ,'America/Atikokan'
                    ,'America/Atka'
                    ,'America/Bahia'
                    ,'America/Bahia_Banderas'
                    ,'America/Barbados'
                    ,'America/Belem'
                    ,'America/Belize'
                    ,'America/Blanc-Sablon'
                    ,'America/Boa_Vista'
                    ,'America/Bogota'
                    ,'America/Boise'
                    ,'America/Cambridge_Bay'
                    ,'America/Campo_Grande'
                    ,'America/Cancun'
                    ,'America/Caracas'
                    ,'America/Cayenne'
                    ,'America/Cayman'
                    ,'America/Chicago'
                    ,'America/Chihuahua'
                    ,'America/Ciudad_Juarez'
                    ,'America/Coral_Harbour'
                    ,'America/Costa_Rica'
                    ,'America/Coyhaique'
                    ,'America/Creston'
                    ,'America/Cuiaba'
                    ,'America/Curacao'
                    ,'America/Danmarkshavn'
                    ,'America/Dawson'
                    ,'America/Dawson_Creek'
                    ,'America/Denver'
                    ,'America/Detroit'
                    ,'America/Dominica'
                    ,'America/Edmonton'
                    ,'America/Eirunepe'
                    ,'America/El_Salvador'
                    ,'America/Ensenada'
                    ,'America/Fort_Nelson'
                    ,'America/Fortaleza'
                    ,'America/Glace_Bay'
                    ,'America/Goose_Bay'
                    ,'America/Grand_Turk'
                    ,'America/Grenada'
                    ,'America/Guadeloupe'
                    ,'America/Guatemala'
                    ,'America/Guayaquil'
                    ,'America/Guyana'
                    ,'America/Halifax'
                    ,'America/Havana'
                    ,'America/Hermosillo'
                    ,'America/Indiana/Indianapolis'
                    ,'America/Indiana/Knox'
                    ,'America/Indiana/Marengo'
                    ,'America/Indiana/Petersburg'
                    ,'America/Indiana/Tell_City'
                    ,'America/Indiana/Vevay'
                    ,'America/Indiana/Vincennes'
                    ,'America/Indiana/Winamac'
                    ,'America/Inuvik'
                    ,'America/Iqaluit'
                    ,'America/Jamaica'
                    ,'America/Juneau'
                    ,'America/Kentucky/Louisville'
                    ,'America/Kentucky/Monticello'
                    ,'America/Kralendijk'
                    ,'America/La_Paz'
                    ,'America/Lima'
                    ,'America/Los_Angeles'
                    ,'America/Lower_Princes'
                    ,'America/Maceio'
                    ,'America/Managua'
                    ,'America/Manaus'
                    ,'America/Marigot'
                    ,'America/Martinique'
                    ,'America/Matamoros'
                    ,'America/Mazatlan'
                    ,'America/Menominee'
                    ,'America/Merida'
                    ,'America/Metlakatla'
                    ,'America/Mexico_City'
                    ,'America/Miquelon'
                    ,'America/Moncton'
                    ,'America/Monterrey'
                    ,'America/Montevideo'
                    ,'America/Montreal'
                    ,'America/Montserrat'
                    ,'America/Nassau'
                    ,'America/New_York'
                    ,'America/Nipigon'
                    ,'America/Nome'
                    ,'America/Noronha'
                    ,'America/North_Dakota/Beulah'
                    ,'America/North_Dakota/Center'
                    ,'America/North_Dakota/New_Salem'
                    ,'America/Nuuk'
                    ,'America/Ojinaga'
                    ,'America/Panama'
                    ,'America/Pangnirtung'
                    ,'America/Paramaribo'
                    ,'America/Phoenix'
                    ,'America/Port-au-Prince'
                    ,'America/Port_of_Spain'
                    ,'America/Porto_Acre'
                    ,'America/Porto_Velho'
                    ,'America/Puerto_Rico'
                    ,'America/Punta_Arenas'
                    ,'America/Rainy_River'
                    ,'America/Rankin_Inlet'
                    ,'America/Recife'
                    ,'America/Regina'
                    ,'America/Resolute'
                    ,'America/Rio_Branco'
                    ,'America/Santa_Isabel'
                    ,'America/Santarem'
                    ,'America/Santiago'
                    ,'America/Santo_Domingo'
                    ,'America/Sao_Paulo'
                    ,'America/Scoresbysund'
                    ,'America/Shiprock'
                    ,'America/Sitka'
                    ,'America/St_Barthelemy'
                    ,'America/St_Johns'
                    ,'America/St_Kitts'
                    ,'America/St_Lucia'
                    ,'America/St_Thomas'
                    ,'America/St_Vincent'
                    ,'America/Swift_Current'
                    ,'America/Tegucigalpa'
                    ,'America/Thule'
                    ,'America/Thunder_Bay'
                    ,'America/Tijuana'
                    ,'America/Toronto'
                    ,'America/Tortola'
                    ,'America/Vancouver'
                    ,'America/Virgin'
                    ,'America/Whitehorse'
                    ,'America/Winnipeg'
                    ,'America/Yakutat'
                    ,'America/Yellowknife'
                    ,'Antarctica/Casey'
                    ,'Antarctica/Davis'
                    ,'Antarctica/DumontDUrville'
                    ,'Antarctica/Macquarie'
                    ,'Antarctica/Mawson'
                    ,'Antarctica/McMurdo'
                    ,'Antarctica/Palmer'
                    ,'Antarctica/Rothera'
                    ,'Antarctica/Syowa'
                    ,'Antarctica/Troll'
                    ,'Antarctica/Vostok'
                    ,'Arctic/Longyearbyen'
                    ,'Asia/Aden'
                    ,'Asia/Almaty'
                    ,'Asia/Amman'
                    ,'Asia/Anadyr'
                    ,'Asia/Aqtau'
                    ,'Asia/Aqtobe'
                    ,'Asia/Ashgabat'
                    ,'Asia/Atyrau'
                    ,'Asia/Baghdad'
                    ,'Asia/Bahrain'
                    ,'Asia/Baku'
                    ,'Asia/Bangkok'
                    ,'Asia/Barnaul'
                    ,'Asia/Beirut'
                    ,'Asia/Bishkek'
                    ,'Asia/Brunei'
                    ,'Asia/Chita'
                    ,'Asia/Choibalsan'
                    ,'Asia/Chongqing'
                    ,'Asia/Colombo'
                    ,'Asia/Damascus'
                    ,'Asia/Dhaka'
                    ,'Asia/Dili'
                    ,'Asia/Dubai'
                    ,'Asia/Dushanbe'
                    ,'Asia/Famagusta'
                    ,'Asia/Gaza'
                    ,'Asia/Harbin'
                    ,'Asia/Hebron'
                    ,'Asia/Ho_Chi_Minh'
                    ,'Asia/Hong_Kong'
                    ,'Asia/Hovd'
                    ,'Asia/Irkutsk'
                    ,'Asia/Istanbul'
                    ,'Asia/Jakarta'
                    ,'Asia/Jayapura'
                    ,'Asia/Jerusalem'
                    ,'Asia/Kabul'
                    ,'Asia/Kamchatka'
                    ,'Asia/Karachi'
                    ,'Asia/Kashgar'
                    ,'Asia/Kathmandu'
                    ,'Asia/Khandyga'
                    ,'Asia/Kolkata'
                    ,'Asia/Krasnoyarsk'
                    ,'Asia/Kuala_Lumpur'
                    ,'Asia/Kuching'
                    ,'Asia/Kuwait'
                    ,'Asia/Macau'
                    ,'Asia/Magadan'
                    ,'Asia/Makassar'
                    ,'Asia/Manila'
                    ,'Asia/Muscat'
                    ,'Asia/Nicosia'
                    ,'Asia/Novokuznetsk'
                    ,'Asia/Novosibirsk'
                    ,'Asia/Omsk'
                    ,'Asia/Oral'
                    ,'Asia/Phnom_Penh'
                    ,'Asia/Pontianak'
                    ,'Asia/Pyongyang'
                    ,'Asia/Qatar'
                    ,'Asia/Qostanay'
                    ,'Asia/Qyzylorda'
                    ,'Asia/Riyadh'
                    ,'Asia/Sakhalin'
                    ,'Asia/Samarkand'
                    ,'Asia/Seoul'
                    ,'Asia/Shanghai'
                    ,'Asia/Singapore'
                    ,'Asia/Srednekolymsk'
                    ,'Asia/Taipei'
                    ,'Asia/Tashkent'
                    ,'Asia/Tbilisi'
                    ,'Asia/Tehran'
                    ,'Asia/Tel_Aviv'
                    ,'Asia/Thimphu'
                    ,'Asia/Tokyo'
                    ,'Asia/Tomsk'
                    ,'Asia/Ulaanbaatar'
                    ,'Asia/Urumqi'
                    ,'Asia/Ust-Nera'
                    ,'Asia/Vientiane'
                    ,'Asia/Vladivostok'
                    ,'Asia/Yakutsk'
                    ,'Asia/Yangon'
                    ,'Asia/Yekaterinburg'
                    ,'Asia/Yerevan'
                    ,'Atlantic/Azores'
                    ,'Atlantic/Bermuda'
                    ,'Atlantic/Canary'
                    ,'Atlantic/Cape_Verde'
                    ,'Atlantic/Faroe'
                    ,'Atlantic/Jan_Mayen'
                    ,'Atlantic/Madeira'
                    ,'Atlantic/Reykjavik'
                    ,'Atlantic/South_Georgia'
                    ,'Atlantic/St_Helena'
                    ,'Atlantic/Stanley'
                    ,'Australia/Adelaide'
                    ,'Australia/Brisbane'
                    ,'Australia/Broken_Hill'
                    ,'Australia/Canberra'
                    ,'Australia/Currie'
                    ,'Australia/Darwin'
                    ,'Australia/Eucla'
                    ,'Australia/Hobart'
                    ,'Australia/Lindeman'
                    ,'Australia/Lord_Howe'
                    ,'Australia/Melbourne'
                    ,'Australia/Perth'
                    ,'Australia/Sydney'
                    ,'Australia/Yancowinna'
                    ,'CET'
                    ,'CST6CDT'
                    ,'EET'
                    ,'EST'
                    ,'EST5EDT'
                    ,'Etc/GMT'
                    ,'Etc/GMT+0'
                    ,'Etc/GMT+1'
                    ,'Etc/GMT+10'
                    ,'Etc/GMT+11'
                    ,'Etc/GMT+12'
                    ,'Etc/GMT+2'
                    ,'Etc/GMT+3'
                    ,'Etc/GMT+4'
                    ,'Etc/GMT+5'
                    ,'Etc/GMT+6'
                    ,'Etc/GMT+7'
                    ,'Etc/GMT+8'
                    ,'Etc/GMT+9'
                    ,'Etc/GMT-0'
                    ,'Etc/GMT-1'
                    ,'Etc/GMT-10'
                    ,'Etc/GMT-11'
                    ,'Etc/GMT-12'
                    ,'Etc/GMT-13'
                    ,'Etc/GMT-14'
                    ,'Etc/GMT-2'
                    ,'Etc/GMT-3'
                    ,'Etc/GMT-4'
                    ,'Etc/GMT-5'
                    ,'Etc/GMT-6'
                    ,'Etc/GMT-7'
                    ,'Etc/GMT-8'
                    ,'Etc/GMT-9'
                    ,'Etc/GMT0'
                    ,'Etc/Greenwich'
                    ,'Etc/UCT'
                    ,'Etc/UTC'
                    ,'Etc/Universal'
                    ,'Etc/Zulu'
                    ,'Europe/Amsterdam'
                    ,'Europe/Andorra'
                    ,'Europe/Astrakhan'
                    ,'Europe/Athens'
                    ,'Europe/Belfast'
                    ,'Europe/Belgrade'
                    ,'Europe/Berlin'
                    ,'Europe/Bratislava'
                    ,'Europe/Brussels'
                    ,'Europe/Bucharest'
                    ,'Europe/Budapest'
                    ,'Europe/Busingen'
                    ,'Europe/Chisinau'
                    ,'Europe/Copenhagen'
                    ,'Europe/Dublin'
                    ,'Europe/Gibraltar'
                    ,'Europe/Guernsey'
                    ,'Europe/Helsinki'
                    ,'Europe/Isle_of_Man'
                    ,'Europe/Istanbul'
                    ,'Europe/Jersey'
                    ,'Europe/Kaliningrad'
                    ,'Europe/Kirov'
                    ,'Europe/Kyiv'
                    ,'Europe/Lisbon'
                    ,'Europe/Ljubljana'
                    ,'Europe/London'
                    ,'Europe/Luxembourg'
                    ,'Europe/Madrid'
                    ,'Europe/Malta'
                    ,'Europe/Mariehamn'
                    ,'Europe/Minsk'
                    ,'Europe/Monaco'
                    ,'Europe/Moscow'
                    ,'Europe/Nicosia'
                    ,'Europe/Oslo'
                    ,'Europe/Paris'
                    ,'Europe/Podgorica'
                    ,'Europe/Prague'
                    ,'Europe/Riga'
                    ,'Europe/Rome'
                    ,'Europe/Samara'
                    ,'Europe/San_Marino'
                    ,'Europe/Sarajevo'
                    ,'Europe/Saratov'
                    ,'Europe/Simferopol'
                    ,'Europe/Skopje'
                    ,'Europe/Sofia'
                    ,'Europe/Stockholm'
                    ,'Europe/Tallinn'
                    ,'Europe/Tirane'
                    ,'Europe/Tiraspol'
                    ,'Europe/Ulyanovsk'
                    ,'Europe/Vaduz'
                    ,'Europe/Vatican'
                    ,'Europe/Vienna'
                    ,'Europe/Vilnius'
                    ,'Europe/Volgograd'
                    ,'Europe/Warsaw'
                    ,'Europe/Zagreb'
                    ,'Europe/Zurich'
                    ,'Factory'
                    ,'GMT'
                    ,'HST'
                    ,'Indian/Antananarivo'
                    ,'Indian/Chagos'
                    ,'Indian/Christmas'
                    ,'Indian/Cocos'
                    ,'Indian/Comoro'
                    ,'Indian/Kerguelen'
                    ,'Indian/Mahe'
                    ,'Indian/Maldives'
                    ,'Indian/Mauritius'
                    ,'Indian/Mayotte'
                    ,'Indian/Reunion'
                    ,'MET'
                    ,'MST'
                    ,'MST7MDT'
                    ,'PST8PDT'
                    ,'Pacific/Apia'
                    ,'Pacific/Auckland'
                    ,'Pacific/Bougainville'
                    ,'Pacific/Chatham'
                    ,'Pacific/Chuuk'
                    ,'Pacific/Easter'
                    ,'Pacific/Efate'
                    ,'Pacific/Fakaofo'
                    ,'Pacific/Fiji'
                    ,'Pacific/Funafuti'
                    ,'Pacific/Galapagos'
                    ,'Pacific/Gambier'
                    ,'Pacific/Guadalcanal'
                    ,'Pacific/Guam'
                    ,'Pacific/Honolulu'
                    ,'Pacific/Johnston'
                    ,'Pacific/Kanton'
                    ,'Pacific/Kiritimati'
                    ,'Pacific/Kosrae'
                    ,'Pacific/Kwajalein'
                    ,'Pacific/Majuro'
                    ,'Pacific/Marquesas'
                    ,'Pacific/Midway'
                    ,'Pacific/Nauru'
                    ,'Pacific/Niue'
                    ,'Pacific/Norfolk'
                    ,'Pacific/Noumea'
                    ,'Pacific/Pago_Pago'
                    ,'Pacific/Palau'
                    ,'Pacific/Pitcairn'
                    ,'Pacific/Pohnpei'
                    ,'Pacific/Port_Moresby'
                    ,'Pacific/Rarotonga'
                    ,'Pacific/Saipan'
                    ,'Pacific/Samoa'
                    ,'Pacific/Tahiti'
                    ,'Pacific/Tarawa'
                    ,'Pacific/Tongatapu'
                    ,'Pacific/Wake'
                    ,'Pacific/Wallis'
                    ,'Pacific/Yap'
                    ,'UTC'
                    ,'WET'
                    )

        if tdctl == '4':
            timezone = input('Enter timezone: ')
            if timezone in timezones:
                os.system('timedatectl set-timezone ' + timezone)
            else:
                exit(0)
        else:
            exit(0)
        
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
    print('3. permissions')
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
            print('\nCommands')
            print('-------------------------------------')
            print('1. add blank file')
            print('2. copy command output to a file')
            print('3. append a file')
            
            add_command = input('\nChoose an option: ')
            
            if add_command == '1':
                file = input('Enter file to modify: ')
                if file != '':
                    os.system('touch ' + file)
                else:
                    exit(0)
            
            if add_command == '2':
                add_file = input('Do you want to make a file from a command / file?: ')
                if add_file == 'y':
                    file = input('Enter file to make: ')
                    command = input('Enter command to copy output to a file: ')
                    if file != '' and command != '':
                        os.system(command + ' > ' + file)
                if add_file == 'n':
                    exit(0)
            
            if add_command == '3':
                    append_file = input('Do you want to append an existing file?: ')
                    if append_file == 'y':
                        file = input('Enter file to modify: ')
                        command = input('Enter new command to copy output to the file: ')
                        if file != '' and command != '':
                            os.system(command + ' >> ' + file)
                    if append_file == 'n':
                        exit(0)
        
        
        if add_or_del_files == '2':
            file = input('Enter file to modify: ')
            if file != '':
                os.system('rm' + ' ' + file)
            else:
                exit(0)
                
    if files_command == '2':
        print('\nCommands')
        print('-------------------------------------')
        print('1. add directories')
        print('2. delete directories')
        
        add_or_del_folders = input('\nChoose an option: ')
        
        if add_or_del_folders == '1':
            folder = input('Enter folder to modify: ')
            if folder != '':
                os.system('mkdir ' + folder + '/')
            else:
                exit(0)
    
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
        print('1. directory permssions')
        print('2. file permissions')

        perm_command = input('\nChoose an option: ')
        
        if perm_command == '2':
            print('\nCommands')
            print('-------------------------------------')
            print('1. make files executable')
            print('2. make files not executable')
          
            perm_files_command = input('\nChoose an option: ')
            
            if perm_files_command == '1':
                file = input('Enter file to modify: ')
                command = input('Enter command: ')
                if command == 'chmod +x':
                    os.system(command + ' ' + file)
                        
            if perm_files_command == '2':
                file = input('Enter file to modify: ')
                command = input('Enter command: ')
                if command == 'chmod -x':
                    os.system(command + ' ' + file)  
                    
            else:
                exit(0)
                
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
                print('2. disable ufw')
                print('3. enable ufw')
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
                    os.system('sudo ufw disable')
                    
                if ufw_command == '3':
                    os.system('sudo ufw enable')
                    
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


        
                    
# Need some help?
            
if category == '0':

    command_list = ('passwd', 'usermod', 'sudo', 'su', 'df', 'free', 'echo', 'id', 'hostnamectl', 'htop', 'apt', 'dnf', 'pacman', 'install', 'remove', 'localectl', 'ls', 'lsblk', 'ls', 'lsblk', 'lscpu', 'lshw', 'lsmem', 'lsmod', 'lspci', 'lsusb', 'pwd', 'shutdown', 'systemctl', 'timedatectl', 'top', 'touch', 'rm', 'rmdir', 'chmod', 'cat', 'ufw', 'gufw', 'arp', 'dig', 'ifconfig', 'ip', 'netstat', 'nmap', 'nslookup', 'ping', 'tcpdump', 'traceroute', 'nano', 'vi', 'vim', 'tree', 'dmesg', 'journalctl', 'history', 'blkid', 'firewalld', 'iptables', 'ssh', 'timeshift')
    
    command = input('Enter command to need help with?: ')
    if command in command_list:
        os.system('man' + ' ' + command)

else:
    exit(0)

# End of Code
