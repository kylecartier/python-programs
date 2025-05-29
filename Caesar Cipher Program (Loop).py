import string

def main():
    
    # Define cipher function
    def cipher(text, shift, alphabs):

        # Define shifting alphabet function
        def shift_alphab(alphab):
            return alphab[shift:] + alphab[:shift]

        # Show the shifted alphabet
        shifted_alphabs = tuple(map(shift_alphab, alphabs))

        # Show the final alphabet
        final_alphab = "".join(alphabs)

        # Show the shifted alphabet
        final_shifted_alphab = "".join(shifted_alphabs)

        # Traslate both final alphabet and final shifted alphabet
        table = str.maketrans(final_alphab, final_shifted_alphab)

        # Return the table
        return text.translate(table)

    # Ask user for input
    pt = input("Enter a word: ")

    # Encrypt the code  
    while True:
        if pt != "@dm1n$":
            print("Try again, you're still in the loop")
            pt = input("Enter another word: ")

        else:
            break

    # You're out of the loop!        
    print("Good job, you encrypted the code!")
    print("You're not done yet......")

    # Decrypt the code now........
    while True:
        if cipher != "@mv1w$":
            cipher = input("Enter the code: ")

        if cipher != "@mv1w$":
            print("Try again, almost out of the loop.....")
            
        else:
            break

    print(pt)
    print("You decrypted the code!")
    print("All done!")
            
    # End of Code

main()
