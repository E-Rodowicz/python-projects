# Coursework Assessment 1
# Name: Emanuel Rodowicz

# A Caesar Cipher Program
import os.path

def welcome():
    """Displays a welcome message."""
    print("Welcome to the Caesar Cipher\n" \
    "This program encrypts and decrypts text with the Caesar Cipher.")

def enter_message():
    """
    A function for part 1 of the assignment, unused in final version as message_or_file() is used
     instead. Question the user for input regarding mode, message, and shift amount.
    """
    mode = ''
    message = ''
    shift = 0

# Asking if the user is encrytping or decrypting and only accepting
# "e" or "d" before breaking the loop.
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d): ")
        if mode in ("e", "d"):
            break
        print("Invalid Mode")

# Asking what message they would like to encrypt/decrypt and looping until the string is
# letters only, then converting the message to uppercase and breaking the loop.
    while message == '':
        if mode == "e":
            message = input("What message would you like to encrypt: ")
        else:
            message = input("What message would you like to decrypt: ")
        if all(char.isalpha() or char.isspace() for char in message):
            message = message.upper()
            break
        print("Invalid Input")

# Asking by how many letters they would like to shift and returning errors until
# the input is an integer between 1 and 25.
    while shift == 0:
        try:
            shift = int(input("What is the shift number: "))
            if shift >= 1 and shift <= 25:
                break
            print("Invalid Shift")
        except ValueError:
            print("Invalid Shift")
    return (mode, message, shift)

def encrypt(message,shift):
    """Encrypts the message by shifting the letters by the shift number"""
    encrypted = ''
    for char in message.upper():
        if char.isalpha():
            encrypted += chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            encrypted += char
    return encrypted

def decrypt(message,shift):
    """Decrypts the message by shifting the letters by the shift number"""
    decrypted = ''
    for char in message.upper():
        if char.isalpha():
            decrypted += chr((ord(char) - 65 - shift) % 26 + 65)
        else:
            decrypted += char
    return decrypted


def process_file(filename, mode, shift):
    """
    This opens the file you want changed in read-mode, converts all the letters one line
    at a time to uppercase (while leaving all of the other characters and spaces as they are)
    and adds the line to the new file, before doing the same with the next line.
    Once all the lines are done, it closes the file handle and returns the message list
    to main().
    """
    list_messages = []
    with open(filename, 'r', encoding='utf-8') as file_handle:
        for base_line in file_handle:
            line = base_line.rstrip('\n\r')
            upper_conversion = ''.join(char.upper() if char.isalpha() else char for char in line)
            if mode == "e":
                ready_line = encrypt(upper_conversion, shift)
            else:
                ready_line = decrypt(upper_conversion, shift)
            list_messages.append(ready_line)
    return list_messages


def write_messages(lines):
    """Writes the processed lines to results.txt, one line at a time."""
    if lines is None:
        return
    with open('results.txt', 'w', encoding='utf-8') as file_handle:
        for current_line in lines:
            file_handle.write(current_line + '\n')
    print("Output written to results.txt")
    return

# Checking if the file exists
def is_file(filename):
    """Checks if the file exists."""
    return os.path.isfile(filename)


def message_or_file():
    """
    Asks the user if they would like to read from a file or the console,
    then asks for the message or filename (dependant on if file or console was chosen before),
    as well as mode and shift amount.
    """
    mode = ''
    filename = None
    message = None
    shift = 0

# Asking if they are encrytping or decrypting and only accepting "e" or "d" before breaking the loop
    while True:
        mode = input("Would you like to encrypt (e) or decrypt (d)? ")
        if mode in ("e", "d"):
            break
        print("Invalid Mode")

# Asking if they would like to read from a file or the console and only accepting
# "f" or "c" before breaking the loop.
    while True:
        file_or_console = input("Would you like to read from a file (f) or the console (c): ")
        if file_or_console in ("f", "c"):
            break
        print("Invalid Choice")

# Asking what message they would like to encrypt/decrypt and looping until the string is
# letters only, then converting the message to uppercase.
    if file_or_console == "c":
        if mode == "e":
            message = input("What message would you like to encrypt: ")
        else:
            message = input("What message would you like to decrypt: ")

# Is file was chosen, the user is asked for a filename.
    else:
        while True:
            filename = input("Enter a filename: ")
            correct_filename = is_file(filename)
            if correct_filename is True:
                break
            print("Invalid Filename")

# Asking by how many letters they would like to shift and returning errors until
# the input is an integer between 1 and 25.
    while shift < 1 or shift > 25:
        try:
            shift = int(input("What is the shift number: "))
            if shift >= 1 and shift <= 25:
                break
            print("Invalid Shift")
        except ValueError:
            print("Invalid Shift")

    return (mode, message, filename, shift)

"""
MAIN DRIVER FUNCTION
----------------------------------------------------------------------------------------------
Requirements:
    • Prompt users to select a mode: encrypt (e) or decrypt (d).
    • Check if the mode the user entered is valid.
    If not, continue to prompt the user until a valid mode is selected.
    • Prompt the user for the message they would like to encrypt/decrypt.
    • encrypt/decrypt the message as appropriate and print the output.
    • Prompt the user whether they would like to encrypt/decrypt another message.
        • Check if the user has entered a valid input (y/n).
          If not, continue to prompt the user until they enter a valid response.
          Depending upon the response you should either:
            • End the program if the user selects no.
            • Proceed directly to step 2 if the user says yes.
    • Your program should be as close as possible to the example shown in the assessment specification.
"""
def main():
    """
    The main driver function for the program. Calls in the weclome function,
    after which it calls in the message_or_file() function to get the mode, message/filename
    and shift amount. If a message was entered it calls in either the encrypt() or decrypt()
    function and prints the result. If a filename was entered it calls in process_file() to
    get the list of processed lines and then calls in write_messages() to write the lines to
    results.txt. Finally, it asks if the user would like to restart the program or end it.
    """
    welcome()
    while True:
        mode, message, filename, shift = message_or_file()
        if filename is None:
            if mode == "e":
                encrypted = encrypt(message, shift)
                print(encrypted)
            else:
                decrypted = decrypt(message, shift)
                print(decrypted)
        else:
            list_messages = process_file(filename, mode, shift)
            write_messages(list_messages)

        while True:
            restart = input("Would you like to encrypt/decrypt another message? (y/n): ")
            if restart == "y":
                break
            if restart == "n":
                print("Thanks for using the program, goodbye!")
                return
            print("Invalid Input")

# Program execution begins here
if __name__ == '__main__':
    main()
