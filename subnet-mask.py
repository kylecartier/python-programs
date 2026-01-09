#!/usr/bin/env python3

# Subnet Mask

first_octet = input("Enter the first octet: ")
second_octet = input("Enter the second octet: ")
third_octet = input("Enter the third octet: ")
fourth_octet = input("Enter the fourth octet: ")

# Numbers for the subnet mask

octet_numbers = (128, 192, 224, 240, 248, 252, 254, 255)
finished_mask = (255, )
zero = (0, )

# If staatements for subnet classes

# Class A Subnet

try:
    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if first_octet in octet_numbers:
        if second_octet in zero:
            if third_octet in zero:
                if fourth_octet in zero:
                    subnet_mask_a = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    result_a = (f'{subnet_mask_a} is a class A subnet.')
                    print(result_a)
                    print("This subnet mask is used with ip addresses that range from 1 to 127.")

except:
    exit(0)

# Class B Subnet

try:
    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if first_octet in finished_mask:
        if second_octet in octet_numbers:
            if third_octet in zero:
                if fourth_octet in zero:
                    subnet_mask_b = (f'{first_octet}.{second_octet}.0.0')
                    result_b = (f'{subnet_mask_b} is a class B subnet.')
                    print(result_b)
                    print("This subnet mask is used with ip addresses that range from 128 to 191.")
except:
    exit(0)

# Class C Subnet

try:
    first_octet = int(first_octet)
    second_octet = int(second_octet)
    third_octet = int(third_octet)
    fourth_octet = int(fourth_octet)

    if first_octet in finished_mask:
        if second_octet in finished_mask:
            if third_octet in octet_numbers:
                if fourth_octet in zero:
                    subnet_mask_c = (f'{first_octet}.{second_octet}.{third_octet}.{fourth_octet}')
                    result_c = (f'{subnet_mask_c} is a class C subnet.')
                    print(result_c)
                    print("This subnet mask is used with ip addresses that range from 192 to 223.")
except:
    exit(0)
    
# End of Code

