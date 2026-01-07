#!/usr/bin/env python3

# IP Addressing

# Prompt user to put in an IP address (Each individual octet)

first_octet = int(input("Enter the first octet: "))
second_octet = int(input('Enter the second octet '))
third_octet = int(input('Enter the third octet: '))
fourth_octet = int(input('Enter the fourth octet: '))

# If staatements for IP classes, loopback address, APIPA address, and Private IP addresses

# Class A, Loopback, and Class A (Private)

if first_octet in range(1, 128):
    if second_octet <= 255:
        if third_octet <= 255:
            if fourth_octet <= 255:
                ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                result = (f'{ip} is a class A address.')
                print(result)
            if first_octet == 127 and fourth_octet <= 255:
                ip = (f'127.{second_octet}.{third_octet}.{fourth_octet}')
                print("This is a loopback address.")
            if first_octet == 10 and fourth_octet <= 255:
                ip = (f'10.{second_octet}.{third_octet}.{fourth_octet}')
                print("This is a private class A address.")

# Class B, APIPA, and Class B (Private)

if first_octet in range(128, 192):
    if second_octet <= 255:
        if third_octet <= 255:
            if fourth_octet <= 255:
                ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                result = (f'{ip} is a class B address.')
                print(result)
            if first_octet == 169 and fourth_octet <= 255:
                ip = (f'169.{second_octet}.{third_octet}.{fourth_octet}')
                print("This is an APIPA address.") 
            if first_octet == 172 and fourth_octet <= 255:
                ip = (f'172.{second_octet}.{third_octet}.{fourth_octet}')
                print("This is a private class B address.")

# Class C and Class C (Private)

if first_octet in range(192, 224):
    if second_octet <= 255:
        if third_octet <= 255:
            if fourth_octet <= 255:
                ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                result = (f'{ip} is a class C address.')
                print(result)
            if first_octet == 192 and fourth_octet <= 255:
                ip = (f'192.{second_octet}.{third_octet}.{fourth_octet}')
                print("This is a private class C address.")


# End of Code

