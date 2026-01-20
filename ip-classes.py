#!/usr/bin/env python3

# IP Classes

# Prompt user to put in an IP address (Each individual octet)

first_octet = input("Enter the first octet: ")
second_octet = input("Enter the second octet: ")
third_octet = input("Enter the third octet: ")
fourth_octet = input("Enter the fourth octet: ")

# If staatements for IP classes, loopback address, APIPA address, and Private IP addresses

# Class A, Loopback, and Class A (Private)

try:
    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if first_octet in range(1, 128):
        if second_octet <= 255:
            if third_octet <= 255:
                if fourth_octet <= 255:
                    ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    result = (f'{ip} is a class A address.')
                    print(result)
                if first_octet == 127 and fourth_octet <= 255:
                    ip = (f'127.{second_octet}.{third_octet}.{fourth_octet}')
                    print("This is also a loopback address.")
                if first_octet == 10 and fourth_octet <= 255:
                    ip = (f'10.{second_octet}.{third_octet}.{fourth_octet}')
                    print("This is also a private class A address.")
except:
    exit(0)

# Class B, APIPA, and Class B (Private)

try:
    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if first_octet in range(128, 192):
        if second_octet <= 255:
            if third_octet <= 255:
                if fourth_octet <= 255:
                    ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    result = (f'{ip} is a class B address.')
                    print(result)
                if first_octet == 169 and second_octet == 254:
                    ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    print("This is also an APIPA address.") 
                if first_octet == 172 and second_octet in range (16, 32):
                    ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    print("This is also a private class B address.")

except:
    exit(0)

# Class C and Class C (Private)

try:
    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if first_octet in range(192, 224):
        if second_octet <= 255:
            if third_octet <= 255:
                if fourth_octet <= 255:
                    ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    result = (f'{ip} is a class C address.')
                    print(result)
                if first_octet == 192 and second_octet == 168:
                    ip = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    print("This is also a private class C address.")

except:
    exit(0)

# End of Code
