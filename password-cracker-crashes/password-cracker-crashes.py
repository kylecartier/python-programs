def main():

    import hashlib

    # Make Variable(s)
    
    username = input("What is the username? ")

    # If Else statement

    if username == "Kyle":
        password = input("What is the password? ")
        if password == "Admin1234!":
            print("Good Job!")

        else:
            print("Try again")
            exit(1)

    else:
        print("Try again")
        exit(1)

    # Define fucntion(s) and do try / except statement

    def crack_hash(inputpass):
        try:
            password_file = open("Passwords.txt")
        except:
            print("Cannot open text file")
            print("Make a text file.")
            exit(1)

    # Have the password become known in hash value by encrypting it 

        for password in password_file:
            encpass = password.encode("utf-8")
            digest = hashlib.md5(encpass.strip()).hexdigest()
            
    # IF statement
            
            if digest == inputpass:
                print ("The password is: " + password)

    # Print out the Password

    if __name__ == '__main__':
        crack_hash("a01726b559eeeb5fc287bf0098a22f6c")
        
# End of code!

main()

