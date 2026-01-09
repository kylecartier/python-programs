#!/usr/bin/env python3

# CIDR Notation (Subnetting Calculator)

cidr_notation = input("Enter the cidr notation: ")

# All octets go from 1 - 128 (When counting via ip addresses to get subnet bits, do 2 - 256)

# Formulas for calculating number of networks and hosts

cidr_net_8 = 2**7  # Class A 
cidr_host_8 = 2**24-2
subnet_mask_8 = "255.0.0.0"

# If ip address is a class A

cidr_net_16 = 2**7 * 2**0
cidr_net_9_a = 2**1
cidr_host_9 = 2**23-2
subnet_mask_9 = "255.128.0.0"

cidr_net_16 = 2**7 * 2**1
cidr_net_10_a = 2**2
cidr_host_10 = 2**22-2
subnet_mask_10 = "255.192.0.0"

cidr_net_16 = 2**7 * 2**2
cidr_net_11_a = 2**3
cidr_host_11 = 2**21-2
subnet_mask_11 = "255.224.0.0"

cidr_net_16 = 2**7 * 2**3
cidr_net_12_a = 2**4
cidr_host_12 = 2**20-2
subnet_mask_12 = "255.240.0.0"

cidr_net_13 = 2**7 * 2**4
cidr_net_13_a = 2**5
cidr_host_13 = 2**19-2
subnet_mask_13 = "255.248.0.0"

cidr_net_14 = 2**7 * 2**5
cidr_net_14_a = 2**6
cidr_host_14 = 2**18-2
subnet_mask_14 = "255.252.0.0"

cidr_net_15 = 2**7 * 2**6
cidr_net_15_a = 2**7
cidr_host_15 = 2**17-2
subnet_mask_15 = "255.254.0.0"

cidr_net_16 = 2**7 * 2**7  # Class B
cidr_net_16_a = 2**8
cidr_host_16 = 2**16-2
subnet_mask_16 = "255.255.0.0"

# If ip address is a class A or B

cidr_net_17_a = 2**9
cidr_net_17_b = 2**1
cidr_host_17 = 2**15-2
subnet_mask_17 = "255.255.128.0"

cidr_net_18_a = 2**10
cidr_net_18_b = 2**2
cidr_host_18 = 2**14-2
subnet_mask_18 = "255.255.192.0"

cidr_net_19_a = 2**11
cidr_net_19_b = 2**3
cidr_host_19 = 2**13-2
subnet_mask_19 = "255.255.224.0"

cidr_net_20_a = 2**12
cidr_net_20_b = 2**4
cidr_host_20 = 2**12-2
subnet_mask_20 = "255.255.240.0"

cidr_net_21_a = 2**13
cidr_net_21_b = 2**5
cidr_host_21 = 2**11-2
subnet_mask_21 = "255.255.248.0"

cidr_net_22_a = 2**14
cidr_net_22_b = 2**6
cidr_host_22 = 2**10-2
subnet_mask_22 = "255.255.252.0"

cidr_net_23_a = 2**15
cidr_net_23_b = 2**7
cidr_host_23 = 2**9-2
subnet_mask_23 = "255.255.254.0"

cidr_net_24 = 2**7 * 2**7 * 2**7  # Class C
cidr_net_24_a = 2**16
cidr_net_24_b = 2**8
cidr_host_24 = 2**8-2
subnet_mask_24 = "255.255.255.0"

# If ip address is a class C with /24

cidr_net_25 = 2**1
cidr_host_25 = 2**7-2
subnet_mask_25 = "255.255.255.128"

cidr_net_26 = 2**2
cidr_host_26 = 2**6-2
subnet_mask_26 = "255.255.255.192"

cidr_net_27 = 2**3
cidr_host_27 = 2**5-2
subnet_mask_27 = "255.255.255.224"

cidr_net_28 = 2**4
cidr_host_28 = 2**4-2
subnet_mask_28 = "255.255.255.240"

cidr_net_29 = 2**5
cidr_host_29 = 2**3-2
subnet_mask_29 = "255.255.255.248"

cidr_net_30 = 2**6
cidr_host_30 = 2**2-2
subnet_mask_30 = "255.255.255.252"

cidr_net_31 = 2**7
cidr_host_31 = 2**1
subnet_mask_31 = "255.255.255.254"

cidr_net_32 = 2**8
cidr_host_32 = 0
subnet_mask_32 = "255.255.255.255"

# If statements for when the user enters input at the prompt

try:

    if cidr_notation == "/8":
        print("Number of networks overall:", format(cidr_net_8, ","))
        print("Number of usable hosts per network:", format(cidr_host_8, ","))
        print("The subnet mask is:", (subnet_mask_8))

    if cidr_notation == "/9":
        print("Number of networks if class A ip:", format(cidr_net_9_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_9, ","))
        print("The subnet mask is:", (subnet_mask_9))

    if cidr_notation == "/10":
        print("Number of networks if class A ip:", format(cidr_net_10_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_10, ","))
        print("The subnet mask is:", (subnet_mask_10))

    if cidr_notation == "/11":
        print("Number of networks if class A ip:", format(cidr_net_11_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_11, ","))
        print("The subnet mask is:", (subnet_mask_11))

    if cidr_notation == "/12":
        print("Number of networks if class A ip:", format(cidr_net_12_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_12, ","))
        print("The subnet mask is:", (subnet_mask_12))

    if cidr_notation == "/13":
        print("Number of networks if class A ip:", format(cidr_net_13_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_13, ","))
        print("The subnet mask is:", (subnet_mask_13))

    if cidr_notation == "/14":
        print("Number of networks if class A ip:", format(cidr_net_14_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_14, ","))
        print("The subnet mask is:", (subnet_mask_14))

    if cidr_notation == "/15":
        print("Number of networks if a class A ip::", format(cidr_net_15_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_15, ","))
        print("The subnet mask is:", (subnet_mask_15))

    if cidr_notation == "/16":
        print("Number of networks overall:", format(cidr_net_16, ","))
        print("Number of networks if class A ip:", format(cidr_net_16_a, ","))
        print("Number of usable hosts per network:", format(cidr_host_16, ","))
        print("The subnet mask is:", (subnet_mask_16))

    if cidr_notation == "/17":
        print("Number of networks if a class A ip:", format(cidr_net_17_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_17_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_17, ","))
        print("The subnet mask is:", (subnet_mask_17))

    if cidr_notation == "/18":
        print("Number of networks if class A ip:", format(cidr_net_18_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_18_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_18, ","))
        print("The subnet mask is:", (subnet_mask_18))

    if cidr_notation == "/19":
        print("Number of networks if class A ip:", format(cidr_net_19_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_19_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_19, ","))
        print("The subnet mask is:", (subnet_mask_19))

    if cidr_notation == "/20":
        print("Number of networks if class A ip:", format(cidr_net_20_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_20_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_20, ","))
        print("The subnet mask is:", (subnet_mask_20))

    if cidr_notation == "/21":
        print("Number of networks if class A ip:", format(cidr_net_21_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_21_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_21, ","))
        print("The subnet mask is:", (subnet_mask_21))

    if cidr_notation == "/22":
        print("Number of networks if class A ip:", format(cidr_net_22_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_22_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_22, ","))
        print("The subnet mask is:", (subnet_mask_22))

    if cidr_notation == "/23":
        print("Number of networks if class A ip:", format(cidr_net_23_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_23_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_23, ","))
        print("The subnet mask is:", (subnet_mask_23))

    if cidr_notation == "/24":
        print("Number of networks overall:", format(cidr_net_24, ","))
        print("Number of networks if class A ip:", format(cidr_net_24_a, ","))
        print("Number of networks if class B ip:", format(cidr_net_24_b, ","))
        print("Number of usable hosts per network:", format(cidr_host_24, ","))
        print("The subnet mask is:", (subnet_mask_24))

    if cidr_notation == "/25":
        print("Number of networks if class C ip:", format(cidr_net_25, ","))
        print("Number of usable hosts per network:", format(cidr_host_25, ","))
        print("The subnet mask is:", (subnet_mask_25))

    if cidr_notation == "/26":
        print("Number of networks if claa C ip:", format(cidr_net_26, ","))
        print("Number of usable hosts per network:", format(cidr_host_26, ","))
        print("The subnet mask is:", (subnet_mask_26))

    if cidr_notation == "/27":
        print("Number of networks if claa C ip:", format(cidr_net_27, ","))
        print("Number of usable hosts per network:", format(cidr_host_27, ","))
        print("The subnet mask is:", (subnet_mask_27))

    if cidr_notation == "/28":
        print("Number of networks if claa C ip:", format(cidr_net_28, ","))
        print("Number of usable hosts per network:", format(cidr_host_28, ","))
        print("The subnet mask is:", (subnet_mask_28))

    if cidr_notation == "/29":
        print("Number of networks if claa C ip:", format(cidr_net_29, ","))
        print("Number of usable hosts per network:", format(cidr_host_29, ","))
        print("The subnet mask is:", (subnet_mask_29))

    if cidr_notation == "/30":
        print("Number of networks if claa C ip:", format(cidr_net_30, ","))
        print("Number of usable hosts per network:", format(cidr_host_30, ","))
        print("The subnet mask is:", (subnet_mask_30))

    if cidr_notation == "/31":
        print("Number of networks if claa C ip:", format(cidr_net_31, ","))
        print("Number of usable hosts per network:", format(cidr_host_31, ","))
        print("The subnet mask is:", (subnet_mask_31))

    if cidr_notation == "/32":
        print("Number of networks if claa C ip:", format(cidr_net_32, ","))
        print("Number of usable hosts per network:", format(cidr_host_32, ","))
        print("The subnet mask is:", (subnet_mask_32))

except:
        exit(0)

# Print statement after program is executed

print("\nHave a good day!")

# End of Code



