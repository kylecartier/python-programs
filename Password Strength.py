def main():
    
    # Prompt user for password 
    
    password = input("Enter the password: ")

    # Length of password
    
    length = len(password)

    # If Else Statement
    
    if length <= 1:
        print("Make a password....")
        password = input("Set a password: ")
        print(password)
    if length in range (2, 4):
        print("Very weak!")
        new_password = input("Set new a password: ")
        print(new_password)
    if length in range (4, 8):
        print("Weak")
        new_password = input("Set a new password: ")
        print(new_password)
    if length in range (8, 13):
        print("Decent")
    if length >= 15:
        print("Very good!")
    else:
        print("Have a good day!")

main()

# End of Code    

