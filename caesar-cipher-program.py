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

        # Join the shifted alphabet
        final_shifted_alphab = "".join(shifted_alphabs)

        # Traslate both final alphabet and final shifted alphabet
        table = str.maketrans(final_alphab, final_shifted_alphab)

        # Return the table
        return text.translate(table)

    reg_text = input("Enter text: ")
    print (cipher(reg_text, 9, [string.ascii_uppercase, string.ascii_lowercase]))
    print (cipher(reg_text, -9, [string.ascii_uppercase, string.ascii_lowercase]))
            
    # End of Code

main()
