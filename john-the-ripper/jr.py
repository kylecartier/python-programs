#!/usr/bin/env python3

import os

def main():

# Runs john the ripper
        os.system('zip2john password.zip')
        os.system('zip2john password.zip > hash.txt')
        os.system('john --format=zip hash.txt')
        os.system('rm hash.txt')
        print()
        print("Good job hacking!")

main()
